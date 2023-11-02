from django.urls import path
from .views import GroundStationListCreateView

urlpatterns = [
    path('', GroundStationListCreateView.as_view(), name='ground-station-list-create'),
]
