from urllib.parse import urljoin

from django.conf import settings
from django.db import models

from covidtest.mixins.models import TimestampMixin
from covidtest.utils import constants
from covidtest.utils.validators import validate_phone_number


class TestApplication(TimestampMixin):
    """A class used to represent a Application in Project"""

    address = models.CharField(max_length=255, verbose_name="Адрес проживания")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    gender = models.PositiveSmallIntegerField(
        choices=constants.GENDER_TYPES, verbose_name="Пол"
    )
    phone = models.CharField(
        max_length=13, verbose_name="Телефон", validators=[validate_phone_number]
    )
    status = models.PositiveSmallIntegerField(
        choices=constants.APPLICATION_STATUSES,
        default=constants.CREATED,
        verbose_name="Статус заявки",
    )
    result = models.PositiveSmallIntegerField(
        choices=constants.PCR_TEST_RESULTS,
        default=constants.RESULT_EMPTY,
        verbose_name="Результат теста",
    )
    qr_code = models.ImageField(
        upload_to="qr_codes/",
        blank=True,
        null=True,
        verbose_name="QR код",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name="Пользователь",
    )

    @property
    def get_qr_code(self) -> str:
        return urljoin(settings.SITE_URL, self.qr_code.url)

    @property
    def get_gender_in_str(self) -> str:
        return constants.GENDER_TYPES[self.gender][1]

    @property
    def get_status_in_str(self) -> str:
        return constants.APPLICATION_STATUSES[self.status][1]

    @property
    def get_result_in_str(self) -> str:
        return constants.PCR_TEST_RESULTS[self.result][1]

    class Meta:
        db_table = "application"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return (
            f"{self.pk} - {self.full_name} - {self.address} - "
            f"{self.created_at.strftime('%Y-%m-%d')}"
        )


class Schedule(TimestampMixin):
    """A class used to represent a User in Project"""

    day = models.PositiveSmallIntegerField(
        choices=constants.DAYS_OF_THE_WEEK, verbose_name="День недели"
    )
    date_start = models.DateTimeField(verbose_name="Дата начала")
    date_end = models.DateTimeField(verbose_name="Дата конца")
    application = models.OneToOneField(
        "core.TestApplication",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="schedule",
        verbose_name="Расписание"
    )

    @property
    def get_day(self) -> str:
        return constants.DAYS_OF_THE_WEEK[self.day][1]

    @property
    def get_period(self) -> str:
        return (
            f"{self.get_day}: "
            f"{self.date_start.strftime('%H:%M')} - "
            f"{self.date_end.strftime('%H:%M')}"
        )

    class Meta:
        db_table = "schedule"
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    def __str__(self):
        return f"{self.pk} - {self.get_period}"
