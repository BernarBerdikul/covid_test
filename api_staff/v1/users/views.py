from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.users.serializers import UserSerializer
from covidtest.users.permissions import IsStaff
from covidtest.utils.decorators import query_debugger, response_wrapper


@method_decorator(response_wrapper(), name="dispatch")
class UserViewSet(viewsets.ViewSet):
    """ViewSet to work with User"""

    permission_classes = (IsStaff,)

    @query_debugger
    @action(methods=["GET"], detail=False)
    def get_profile(self, request):
        """method return user profile"""
        return Response(UserSerializer(request.user).data)
