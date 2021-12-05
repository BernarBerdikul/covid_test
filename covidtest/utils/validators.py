from uuid import UUID

import phonenumbers

from covidtest.utils import constants, messages
from covidtest.utils.exceptions import CommonException


def validate_phone_number(value):
    try:
        z = phonenumbers.parse(value, None)
    except Exception:
        raise CommonException(detail=messages.PHONE_INCORRECT)
    if not phonenumbers.is_valid_number(z):
        raise CommonException(detail=messages.PHONE_INCORRECT)


def validate_password(value, key: str = "password"):
    if len(value) < constants.PASSWORD_MIN_LENGTH:
        raise CommonException(detail={f"{key}": messages.PASSWORD_INVALID})
    return value


def valid_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        return False
    return True
