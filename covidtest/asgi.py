import os

import django
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covidtest.settings")
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from api.v1.user_socket.consumers import UserConsumer
from api_staff.v1.staff_socket.consumers import StaffConsumer

ws_urlpatterns = [
    re_path(
        r"ws/staff_socket/(?P<email>[.@\w\d]+)/$",
        StaffConsumer.as_asgi(),
    ),
    re_path(
        r"ws/user_socket/(?P<email>[.@\w\d]+)/$",
        UserConsumer.as_asgi(),
    ),
]

application = ProtocolTypeRouter(
    {
        # Django's ASGI application to handle traditional HTTP requests
        "http": get_asgi_application(),
        # WebSocket chat handler
        "websocket": AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
    }
)
