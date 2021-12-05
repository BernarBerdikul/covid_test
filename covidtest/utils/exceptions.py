import logging

from rest_framework.exceptions import APIException
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_412_PRECONDITION_FAILED,
)
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """overwrite custom exception"""
    response = exception_handler(exc, context)
    if response:
        errors = {}
        for field, value in response.data.items():
            if isinstance(value, list):
                errors[f"{field}"] = f"{value[0]}"
        response.data = {"success": False}
        if hasattr(exc, "detail"):
            response.data["errors"] = exc.detail
        if hasattr(exc, "redirect"):
            response.data["redirect"] = exc.redirect
        if hasattr(exc, "notifications"):
            notifications = exc.notifications
            if exc.notifications is None:
                notifications = []
            response.data["notifications"] = notifications
    return response


class CommonException(APIException):
    def __init__(self, status_code=HTTP_400_BAD_REQUEST, detail={}, notifications=None):
        self.status_code = status_code
        self.detail = detail
        self.notifications = notifications


class NotFoundException(APIException):
    status_code = HTTP_404_NOT_FOUND

    def __init__(self, detail={}, notifications=None):
        self.detail = detail
        self.notifications = notifications


class PreconditionFailedException(APIException):
    status_code = HTTP_412_PRECONDITION_FAILED

    def __init__(self, detail={}, notifications=None):
        self.detail = detail
        self.notifications = notifications


class ForbiddenException(APIException):
    status_code = HTTP_403_FORBIDDEN

    def __init__(self, detail={}, redirect=None, notifications=None):
        self.detail = detail
        self.redirect = redirect
        self.notifications = notifications
