from rest_framework import serializers

from .models import Role, Authorization

class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = '__all__'

class AuthorizationSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)  
    
    class Meta:
        model = Authorization
        fields = ['group_name', 'role', 'satellite_code', 'description', 'created', 'updated']


