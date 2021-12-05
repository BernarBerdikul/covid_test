from rest_framework import serializers

from covidtest.core.models import TestApplication


class CreateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestApplication
        fields = (
            "address",
            "full_name",
            "age",
            "gender",
            "phone",
        )


class ListApplicationSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()
    period = serializers.SerializerMethodField()
    qr_code = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = TestApplication
        fields = (
            "id",
            "full_name",
            "status",
            "result",
            "qr_code",
            "period",
            # detail
            "address",
            "age",
            "gender",
            "phone",
        )

    def get_status(self, obj) -> str:
        return obj.get_status_in_str

    def get_result(self, obj) -> str:
        return obj.get_result_in_str

    def get_period(self, obj) -> str:
        return obj.schedule.get_period

    def get_qr_code(self, obj) -> str:
        return obj.get_qr_code

    def get_gender(self, obj) -> str:
        return obj.get_gender_in_str
