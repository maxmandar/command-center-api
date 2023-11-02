from rest_framework import generics
from .models import GroundStation
from .serializers import GroundStationSerializer

class GroundStationListCreateView(generics.ListCreateAPIView):
    queryset = GroundStation.objects.all()
    serializer_class = GroundStationSerializer
