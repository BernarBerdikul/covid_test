# Generated by Django 3.2.9 on 2021-12-05 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_testapplication_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="testapplication",
            name="schedule",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="application",
                to="core.schedule",
                verbose_name="Расписание",
            ),
        ),
    ]