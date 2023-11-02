from django.urls import path
from . import views

urlpatterns = [
    # Rocket URLs
    path('rockets/', views.RocketList.as_view(), name='rocket-list'),
    path('rockets/create/', views.RocketCreate.as_view(), name='rocket-create'),
    path('rockets/<int:id>/update/', views.RocketUpdate.as_view(), name='rocket-update'),
    path('rockets/<int:id>/destroy/', views.RocketDestroy.as_view(), name='rocket-destroy'),
    
    # Stage URLs
    path('stages/', views.StageList.as_view(), name='stage-list'),
    path('stages/create/', views.StageCreate.as_view(), name='stage-create'),
    path('stages/<int:id>/update/', views.StageUpdate.as_view(), name='stage-update'),
    path('stages/<int:id>/destroy/', views.StageDestroy.as_view(), name='stage-destroy'),
]
