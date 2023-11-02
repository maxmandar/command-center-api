import requests
from rest_framework.permissions import BasePermission
from django.conf import settings

class CustomRolePermission(BasePermission):
    expected_role = 'OPERATOR'  # Set this to whatever role you expect the user to have
    
    def has_permission(self, request, view):
        # Extract the token from the user object, which was attached during the authentication phase
        token = getattr(request.user, 'token', None)
        
        if not token:
            return False  # If there's no token attached to the user, deny permission
        
        # Now, let's check the user's roles using the authorization service
        authz_service_url = settings.AUTHORIZATION_SERVICE_URL
        
        try:
            response = requests.get(authz_service_url, headers={"Authorization": f"Bearer {token}"})
            response.raise_for_status()
            roles_data = response.json()
            user_roles = [role_data['role']['name'] for role_data in roles_data]
            return self.expected_role in user_roles
        except requests.RequestException:
            return False  # Deny permission if there's any issue checking roles or if the user doesn't have the expected role
