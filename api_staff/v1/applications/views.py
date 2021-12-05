from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.applications.serializers import ListApplicationSerializer
from covidtest.core.models import TestApplication
from covidtest.sockets.service import update_socket_status
from covidtest.users.permissions import IsStaff
from covidtest.utils import constants
from covidtest.utils.decorators import query_debugger, response_wrapper
from covidtest.utils.exceptions import CommonException

from .serializers import (
    UpdateResultApplicationSerializer,
    UpdateStatusApplicationSerializer,
)
from .service import get_application_or_404


@method_decorator(response_wrapper(), name="dispatch")
class TestApplicationViewSet(viewsets.ViewSet):
    """ViewSet to work with Application"""

    permission_classes = (IsStaff,)

    @query_debugger
    def list(self, request):
        applications = TestApplication.objects.select_related("schedule").order_by(
            "-id"
        )
        return Response(ListApplicationSerializer(applications, many=True).data)

    @query_debugger
    @action(methods=["PATCH"], detail=False)
    def update_result(self, request):
        pk = request.query_params.get("pk")
        application = get_application_or_404(pk=pk)
        """ update application """
        serializer = UpdateResultApplicationSerializer(
            instance=application, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        application = serializer.save()
        """ update socket """
        update_socket_status(application=application)
        return Response({"result": application.get_result_in_str})

    @query_debugger
    @action(methods=["PATCH"], detail=False)
    def update_status(self, request):
        pk = request.query_params.get("pk")
        application = get_application_or_404(pk=pk)
        """ update application """
        serializer = UpdateStatusApplicationSerializer(
            instance=application, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        application = serializer.save()
        """ update socket """
        update_socket_status(application=application)
        return Response({"status": application.get_status_in_str})

    @query_debugger
    def destroy(self, request, pk=None):
        application = get_application_or_404(pk=pk)
        if application.status != constants.CREATED:
            raise CommonException(detail="Уй бля, незя удалять")
        return Response({})
