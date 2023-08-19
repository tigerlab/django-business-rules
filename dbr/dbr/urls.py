from django.urls import include, path, re_path
from django.contrib import admin

urlpatterns = [
    path("dbr/", include("django_business_rules.urls")),
    re_path(r"^admin/", admin.site.urls),
]
