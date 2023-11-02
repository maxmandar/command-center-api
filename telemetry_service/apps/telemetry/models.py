
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from simple_history.models import HistoricalRecords

# models.py
from django.db import models

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Notify WebSocket when a new message is saved
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "data",  # Group Name
            {
                'type': 'send_notification',
                'message': self.content
            }
        )


class Telemetry(models.Model):
    rocket_code = models.CharField(max_length=255)
    rocket_name = models.CharField(max_length=255)
    stage_code = models.CharField(max_length=255)
    stage_name = models.CharField(max_length=255)
    engine_code = models.CharField(max_length=255)
    engine_name = models.CharField(max_length=255)
    speed = models.FloatField()
    altitude = models.FloatField()
    thrust = models.FloatField()
    isp = models.FloatField()  # ISP: specific impulse
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Notify WebSocket when new telemetry data is saved
        group_name = f"telemetry_{self.rocket_code}_{self.stage_code}"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'send_notification',
                'telemetry_data': {
                    'rocket_code': self.rocket_code,
                    'rocket_name': self.rocket_name,
                    'stage_code': self.stage_code,
                    'stage_name': self.stage_name,
                    'engine_code': self.engine_code,
                    'engine_name': self.engine_name,
                    'speed': self.speed,
                    'altitude': self.altitude,
                    'thrust': self.thrust,
                    'isp': self.isp,
                    'temperature': self.temperature,
                    'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime to string
                }
            }
        )