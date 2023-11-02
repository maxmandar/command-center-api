import requests
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

import logging

logger = logging.getLogger(__name__)

      

class CustomTokenBackend(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return None
        
        token = auth_header.split(" ")[1]
        
        # Validate the token with your authentication service
        auth_service_url = settings.AUTHENTICATION_SERVICE_URL 
        
        try:
            response = requests.get(auth_service_url, headers={"Authorization": f"Bearer {token}"})
            response.raise_for_status()
            user_data = response.json()
            user = SimpleUser(user_data['username'], token)
            return (user, token)
        except requests.RequestException as e:
            logger.error(f"Authentication failed due to: {str(e)}")
            raise AuthenticationFailed('Invalid token or the auth service is currently unreachable.')
        
class SimpleUser:
    """A basic user object just to carry some user information after authentication."""
    
    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.is_authenticated = True  # This indicates that this user instance is authenticated

    # Any other methods or attributes you want the user object to have can be added here.
