from django.contrib import admin
from django.urls import path

from .views import ping


base_prefix = "api/v1/"

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("admin/", admin.site.urls),
]
