from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.settings import api_settings


def get_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def decode_token(token: str):
    payload = jwt_decode_handler(token)
    return payload
