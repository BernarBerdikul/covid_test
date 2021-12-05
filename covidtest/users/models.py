from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from covidtest.mixins.models import TimestampMixin
from covidtest.utils import constants


class UserManager(BaseUserManager):
    """Django Manager class for model User"""

    def create_superuser(self, email, password):
        """overwrite method for superuser creating"""
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.role = constants.ADMIN
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    """A class used to represent a User in Project"""

    first_name = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Имя"
    )
    last_name = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Фамилия"
    )
    role = models.PositiveSmallIntegerField(
        choices=constants.USER_TYPES, default=constants.USER, verbose_name="Роль"
    )
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    USERNAME_FIELD = "email"

    objects = UserManager()

    @property
    def get_role(self):
        return constants.USER_TYPES[self.role][1]

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_staff(self):
        # Anyone who is superuser can enter admin
        return self.is_superuser

    def __str__(self):
        return f"{self.pk} - {self.email} - {self.get_role}"
