# apps/authentication/urls.py

from django.urls import path
from .views import LoginView, LogoutView,RefreshTokenView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-view'),
    path('refresh-token/', RefreshTokenView.as_view(), name='refresh-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
]
