from django.urls import path
from rest_framework.routers import DefaultRouter

from .applications.views import TestApplicationViewSet
from .users.views import UserViewSet
from .staff_socket.views import get_staff_socket

router = DefaultRouter()
router.register("applications", TestApplicationViewSet, basename="applications")
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("socket/", get_staff_socket),
]

urlpatterns += router.urls
