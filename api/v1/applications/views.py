from datetime import datetime, timedelta

from django.db import transaction
from django.utils.decorators import method_decorator
from rest_framework import status, viewsets
from rest_framework.response import Response

from covidtest.core.models import Schedule, TestApplication
from covidtest.sockets.service import update_socket_new_object
from covidtest.users.permissions import IsUser
from covidtest.utils.decorators import query_debugger, response_wrapper

from .serializers import CreateApplicationSerializer, ListApplicationSerializer
from .service import create_qr


@method_decorator(response_wrapper(), name="dispatch")
class TestApplicationViewSet(viewsets.ViewSet):
    """ViewSet to work with Application"""

    permission_classes = (IsUser,)

    @query_debugger
    def list(self, request):
        applications = (
            TestApplication.objects.filter(user_id=request.user.id)
            .select_related("schedule")
            .order_by("-id")
        )
        return Response(ListApplicationSerializer(applications, many=True).data)

    @query_debugger
    @transaction.atomic()
    def create(self, request):
        """create application"""
        serializer_application = CreateApplicationSerializer(data=request.data)
        serializer_application.is_valid(raise_exception=True)
        application = serializer_application.save(user_id=request.user.id)
        """ get last schedule """
        last_schedule = Schedule.objects.last()
        """ get date start """
        date_start = application.created_at
        if last_schedule and last_schedule.date_end > date_start:
            date_start = last_schedule.date_end
        """ get date end """
        date_end: datetime = date_start + timedelta(hours=1)
        day: int = date_start.weekday()
        """ create schedule for application """
        Schedule.objects.create(
            day=day,
            date_start=date_start,
            date_end=date_end,
            application_id=application.id
        )
        create_qr(application=application)
        update_socket_new_object(application=application)
        return Response({}, status=status.HTTP_201_CREATED)
