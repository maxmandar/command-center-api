from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from telemetry_service import consumers

# We will add our websocket routes here later
websocket_urlpatterns = [
    path('ws/test/', consumers.TestConsumer.as_asgi()),
    path('ws/data/', consumers.DataConsumer.as_asgi()),
    path('ws/telemetry/<str:rocket_code>/<str:stage_code>/', consumers.TelemetryDataConsumer.as_asgi()),

]

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    # is added by default
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
})
