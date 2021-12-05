# Generated by Django 3.2.9 on 2021-12-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_testapplication_schedule"),
    ]

    operations = [
        migrations.AddField(
            model_name="testapplication",
            name="qr_code",
            field=models.ImageField(
                blank=True, null=True, upload_to="qr_codes/", verbose_name="QR код"
            ),
        ),
        migrations.AlterField(
            model_name="testapplication",
            name="age",
            field=models.PositiveSmallIntegerField(verbose_name="Возраст"),
        ),
    ]