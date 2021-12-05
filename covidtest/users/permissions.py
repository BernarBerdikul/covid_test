from rest_framework.decorators import permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated

from covidtest.utils import constants

from .models import User


@permission_classes([IsAuthenticated])
class IsUser(BasePermission):
    """Permissions for Student"""

    def has_permission(self, request, view):
        return User.objects.filter(id=request.user.id, role=constants.USER).exists()


@permission_classes([IsAuthenticated])
class IsStaff(BasePermission):
    """Permissions for Admin"""

    def has_permission(self, request, view):
        return User.objects.filter(id=request.user.id, role=constants.STAFF).exists()
