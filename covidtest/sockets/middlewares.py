from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser

from covidtest.users.models import User
from covidtest.utils import constants


@database_sync_to_async
def get_user(email):
    try:
        user = User.objects.get(email=email, role=constants.USER)
        return user
    except User.DoesNotExist:
        return AnonymousUser()


@database_sync_to_async
def get_staff(email):
    try:
        user = User.objects.get(email=email, role=constants.STAFF)
        return user
    except User.DoesNotExist:
        return AnonymousUser()
