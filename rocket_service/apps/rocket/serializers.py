from rest_framework import serializers
from .models import Rocket, Stage

class RocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rocket
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class RocketListSerializer(serializers.ModelSerializer):
    stages = StageSerializer(many=True, read_only=True)  # Nested Serializer for related stages

    class Meta:
        model = Rocket
        fields = ('id', 'name', 'code', 'height', 'mass','stages')  

class RocketDetailSerializer(serializers.ModelSerializer):  # Separate serializer for detail views (e.g. create, update)
    class Meta:
        model = Rocket
        fields = '__all__'