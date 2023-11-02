from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import requests
from django.conf import settings

from .models import Role, Authorization
from .serializers import RoleSerializer, AuthorizationSerializer

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class AuthorizationListCreateView(generics.ListCreateAPIView):
    queryset = Authorization.objects.all()
    serializer_class = AuthorizationSerializer

class AuthorizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Authorization.objects.all()
    serializer_class = AuthorizationSerializer



class UserAuthorizationView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        
        auth_header = request.headers.get('Authorization')
        token = auth_header.split(' ')[1] if auth_header else None

        if not token:
            return Response({"detail": "Token not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        user_info_url = settings.USER_INFO_URL
        headers = {
            'Authorization': f"Bearer {token}"
        }
        response = requests.get(user_info_url, headers=headers)

        # If token has expired or user not found
        if response.status_code == 401:
            return Response({"detail": "Token has expired or is invalid."}, status=status.HTTP_401_UNAUTHORIZED)

        # For other non-200 responses
        elif response.status_code != 200:
            return Response({"detail": "Could not fetch user's information."}, status=status.HTTP_400_BAD_REQUEST)

        user_data = response.json()
        user_groups = [group['name'] for group in user_data['groups']]  # Assuming groups is a list of dicts with 'name' key

        # Get authorizations based on user's groups
        user_authorizations = Authorization.objects.filter(group_name__in=user_groups)
        serializer = AuthorizationSerializer(user_authorizations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)