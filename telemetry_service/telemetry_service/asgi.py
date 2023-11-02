import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import telemetry_service.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telemetry_service.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        telemetry_service.routing.websocket_urlpatterns
    ),
})
