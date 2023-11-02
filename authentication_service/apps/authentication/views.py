
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import requests
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout
from rest_framework import status
from django.conf import settings
import logging


# Create your views here.

logger = logging.getLogger('apps.authentication')

class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        
       
        data = {
            'grant_type': 'password',
            'username': username,
            'password': password,
            'client_id': settings.COMMAND_CENTER_CLIENT_ID,
            'client_secret': settings.COMMAND_CENTER_CLIENT_SECRETE,
        }
        print(data)
      
        response = requests.post(settings.OAUTH2_URL, data=data)
        
        if response.status_code == 200:
            return Response(json.loads(response.text))
        else:
            return Response({'error': 'Invalid credentials'}, status=400)



class RefreshTokenView(APIView):
    authentication_classes = [IsAuthenticated]
    permission_classes = []

    def post(self, request, *args, **kwargs):

        refresh_token = request.data.get("refresh_token")

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': settings.COMMAND_CENTER_CLIENT_ID,
            'client_secret': settings.COMMAND_CENTER_CLIENT_SECRET,
        }

        response = requests.post(settings.OAUTH2_REFRESH_URL, data=data)

        if response.status_code == 200:
            return Response(json.loads(response.text))
        else:
            return Response({'error': 'Invalid refresh token'}, status=400)
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        token = request.auth.token  # Assuming Token Authentication is being used
        data = {
            'token': token,
            'client_id': settings.COMMAND_CENTER_CLIENT_ID,
            'client_secret': settings.COMMAND_CENTER_CLIENT_SECRET,
        }

        response = requests.post(settings.OAUTH2_REVOKE_URL, data=data)

        if response.status_code == 200:
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Failed to revoke token'}, status=status.HTTP_400_BAD_REQUEST)