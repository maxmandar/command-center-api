import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .services.validation_service import validate_token, check_user_role

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = self.scope['query_string'].decode("utf-8").split("=")[1]
        print("token:",token)

        # Validate the token using your authentication service
        user_authorizations, is_valid_token = validate_token(token)

        if not is_valid_token:
            await self.send_error("Invalid token or token has expired.")
            return await self.close()

        # Check if user has the 'OPERATOR' role using the authorization service
        has_operator_role = check_user_role(user_authorizations, "OPERATOR")

        if not has_operator_role:
            await self.send_error("Access denied. You don't have the required role.")
            return await self.close()
        
        await self.accept()
        await self.channel_layer.group_add("data", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("data", self.channel_name)

    # This method is triggered when a new Message instance is saved
    async def send_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

        # Convert message to JSON and send
        # message = event['message']
        # await self.send(text_data=json.dumps({
        # 'telemetry_data': message
        # }))

    async def send_error(self, error_message):
        """
        Send error messages that resemble DRF-styled responses.
        """
        await self.send(text_data=json.dumps({
            'error': error_message
        }))


class TelemetryDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # ... (your token validation code)
        
        self.rocket_code = self.scope['url_route']['kwargs']['rocket_code']
        self.stage_code = self.scope['url_route']['kwargs']['stage_code']

        # Create a dynamic group name based on rocket and stage codes
        self.group_name = f"telemetry_{self.rocket_code}_{self.stage_code}"

        # Join the group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # This method is triggered when telemetry data is saved to the database
    async def send_notification(self, event):
        telemetry_data = event['telemetry_data']
        await self.send(text_data=json.dumps({
            'telemetry_data': telemetry_data
        }))