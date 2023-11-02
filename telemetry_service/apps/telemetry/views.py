from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message, Telemetry
import random
import time

# Create your views here.
class MessageAdder(APIView):

    def post(self, request, *args, **kwargs):
        messages = request.data.get('messages', [])

        for msg in messages:
            Message(content=msg).save()
            time.sleep(1)

        return Response({"message": "Messages added successfully!"}, status=status.HTTP_201_CREATED)
    

class TelemetryAdder(APIView):

    def post(self, request, *args, **kwargs):
        telemetry_data = request.data.get('telemetry', [])

        for data in telemetry_data:
            Telemetry(
                rocket_code=data['rocket_code'],
                rocket_name=data.get('rocket_name', ''),
                stage_code=data['stage_code'],
                stage_name=data.get('stage_name', ''),
                engine_code=data.get('engine_code', ''),
                engine_name=data.get('engine_name', ''),
                speed=data['speed'],
                altitude=data['altitude'],
                thrust=data.get('thrust'),  
                isp=data.get('isp'),       
                temperature=data['temperature'],
                timestamp=data['timestamp']
            ).save()
            time.sleep(1)

        return Response({"message": "Telemetry data added successfully!"}, status=status.HTTP_201_CREATED)


from rest_framework import generics, permissions
from .models import Telemetry
from .serializers import TelemetrySerializer

class TelemetryDataView(generics.ListAPIView):
    serializer_class = TelemetrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        rocket_code = self.request.query_params.get('rocket_code')
        stage_code = self.request.query_params.get('stage_code')
        return Telemetry.objects.filter(rocket_code=rocket_code, stage_code=stage_code)