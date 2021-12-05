from django.urls import path
from rest_framework.routers import DefaultRouter

from .applications.views import TestApplicationViewSet
from .user_socket.views import get_user_socket
from .users.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("applications", TestApplicationViewSet, basename="applications")

urlpatterns = [
    path("socket/", get_user_socket),
]

urlpatterns += router.urls
