from django.urls import include, path

app_name = "api_staff"

urlpatterns = [
    path("v1/", include("api_staff.v1.urls")),
]
