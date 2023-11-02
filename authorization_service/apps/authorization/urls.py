from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', views.RoleRetrieveUpdateDestroyView.as_view(), name='role-detail'),
    path('authorizations/', views.AuthorizationListCreateView.as_view(), name='authorization-list-create'),
    path('authorizations/<int:pk>/', views.AuthorizationRetrieveUpdateDestroyView.as_view(), name='authorization-detail'),
    path('user/', views.UserAuthorizationView.as_view(), name='authorization-user'),
]
