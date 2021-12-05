# Generated by Django 3.2.9 on 2021-12-05 23:16

from django.db import migrations, models

import covidtest.utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        null=True,
                        verbose_name="Время последнего изменения",
                    ),
                ),
                (
                    "day",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "ПН"),
                            (1, "ВТ"),
                            (2, "СР"),
                            (3, "ЧТ"),
                            (4, "ПТ"),
                            (5, "СБ"),
                            (6, "ВС"),
                        ],
                        verbose_name="День недели",
                    ),
                ),
                ("date_start", models.DateTimeField(verbose_name="Дата начала")),
                ("date_end", models.DateTimeField(verbose_name="Дата конца")),
            ],
            options={
                "verbose_name": "Расписание",
                "verbose_name_plural": "Расписание",
                "db_table": "schedule",
            },
        ),
        migrations.CreateModel(
            name="TestApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        null=True,
                        verbose_name="Время последнего изменения",
                    ),
                ),
                (
                    "address",
                    models.CharField(max_length=255, verbose_name="Адрес проживания"),
                ),
                ("full_name", models.CharField(max_length=100, verbose_name="ФИО")),
                ("age", models.PositiveSmallIntegerField(verbose_name="Возраст")),
                (
                    "gender",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Мужской"), (1, "Женский")], verbose_name="Пол"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=13,
                        validators=[covidtest.utils.validators.validate_phone_number],
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Заявка создана"),
                            (1, "Выполняется"),
                            (2, "Обрабатываются результаты"),
                            (3, "Заявка завершена"),
                        ],
                        default=0,
                        verbose_name="Статус заявки",
                    ),
                ),
                (
                    "result",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Пусто"), (1, "Позитивный"), (2, "Негативный")],
                        default=0,
                        verbose_name="Результат теста",
                    ),
                ),
                (
                    "qr_code",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="qr_codes/",
                        verbose_name="QR код",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки",
                "db_table": "application",
            },
        ),
    ]
