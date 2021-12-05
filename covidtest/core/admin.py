from django.contrib import admin

from .models import Schedule, TestApplication


@admin.register(TestApplication)
class TestApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
