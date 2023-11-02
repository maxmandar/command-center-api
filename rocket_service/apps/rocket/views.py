from rest_framework import generics
from .models import Rocket, Stage
from .serializers import RocketSerializer, StageSerializer

from rest_framework import generics
from .models import Rocket, Stage
from .serializers import RocketListSerializer, RocketDetailSerializer, StageSerializer

# Rocket Views
class RocketList(generics.ListAPIView):
    queryset = Rocket.objects.all()
    serializer_class = RocketListSerializer

class RocketCreate(generics.CreateAPIView):
    queryset = Rocket.objects.all()
    serializer_class = RocketDetailSerializer

class RocketUpdate(generics.UpdateAPIView):
    queryset = Rocket.objects.all()
    serializer_class = RocketDetailSerializer
    lookup_field = 'id'

class RocketDestroy(generics.DestroyAPIView):
    queryset = Rocket.objects.all()
    serializer_class = RocketDetailSerializer
    lookup_field = 'id'

# Stage Views
class StageList(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class StageCreate(generics.CreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class StageUpdate(generics.UpdateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    lookup_field = 'id'

class StageDestroy(generics.DestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    lookup_field = 'id'
