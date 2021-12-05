from datetime import datetime

from rest_framework import serializers

from covidtest.authentication import get_token
from covidtest.users.models import User
from covidtest.utils import constants, messages
from covidtest.utils.decorators import query_debugger
from covidtest.utils.exceptions import CommonException, PreconditionFailedException
from covidtest.utils.validators import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registration"""

    password = serializers.CharField()
    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "password_confirm",
        )

    @query_debugger
    def register(self, validated_data):
        """Register new user"""
        email: str = validated_data.get("email")
        password: str = validate_password(
            value=validated_data.get("password"), key="password"
        )
        if password != validated_data.get("password_confirm"):
            raise CommonException(
                detail={
                    "password": messages.PASSWORD_NOT_EQUAL,
                    "password_confirm": messages.PASSWORD_NOT_EQUAL,
                }
            )
        user = User.objects.create(email=email, role=constants.USER)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """Manager Serializer in both console"""

    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "email", "role")

    def get_role(self, obj):
        return obj.get_role


class ChangePasswordSerializer(serializers.Serializer):
    """change password for manager in both console"""

    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        """check if passwords are equal"""
        password = validate_password(attrs["password"])
        password_confirm = validate_password(attrs["password"])
        if password != password_confirm:
            raise CommonException(detail=messages.PASSWORD_NOT_EQUAL)
        return attrs

    def change(self):
        user = self.context["user"]
        user.set_password(self.validated_data["password"])
        user.save()
        return user

    @query_debugger
    def update_email(self):
        """method get User and update his email"""
        manager = User.objects.get(id=self.context["user"].id)
        manager.email = self.validated_data["email"]
        manager.save()
        return manager


class LoginSerializer(serializers.Serializer):
    """Login for manager in both console"""

    email = serializers.CharField()
    password = serializers.CharField()

    @query_debugger
    def user_login(self):
        """after login check device and create new object in model ManagerDevice
        (for each device generate new token)"""
        try:
            user = User.objects.get(email=self.validated_data["email"])
            if not user.check_password(self.validated_data["password"]):
                raise PreconditionFailedException(
                    detail={"password": messages.WRONG_LOGIN_OR_PASSWORD}
                )
        except User.DoesNotExist:
            raise PreconditionFailedException(
                detail={"password": messages.WRONG_LOGIN_OR_PASSWORD}
            )

        token = get_token(user)
        user.last_login = datetime.now()
        user.save()
        return token, user.role
