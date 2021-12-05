from rest_framework import serializers

from covidtest.core.models import TestApplication


class UpdateResultApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestApplication
        fields = ("result",)


class UpdateStatusApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestApplication
        fields = ("status",)
