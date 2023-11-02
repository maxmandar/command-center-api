from django.urls import path
from .views import MessageAdder, TelemetryAdder, TelemetryDataView

urlpatterns = [
    path('add-messages/', MessageAdder.as_view(), name='add-messages'),
    path('add-telemetry/', TelemetryAdder.as_view(), name='add-telemetry'),
    path('history/', TelemetryDataView.as_view(), name='telemetry-history'),

]
