from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("super-secret-admin/", admin.site.urls, name="admin"),
    path("api/", include("api.urls")),
    path("api_staff/", include("api_staff.urls")),
]

if settings.IS_TEST:
    urlpatterns += [
        url(
            r"^api/docs/",
            include_docs_urls(
                title="covidtest documentation",
                authentication_classes=[],
                permission_classes=[permissions.AllowAny],
            ),
        ),
    ]

if settings.IS_LOCAL:
    # This will be used when we launch this locally by runserver
    # On remote server it should be handled by Nginx
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
