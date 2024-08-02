import logging

from django.db import models
from django.http import HttpRequest
from django.views import View
from rest_framework.permissions import BasePermission, DjangoModelPermissions


logger = logging.getLogger("main")


class CustomDjangoModelPermissions(  # type: ignore[misc]
    DjangoModelPermissions
):
    view_permissions: list[str] = ["%(app_label)s.view_%(model_name)s"]
    perms_map: dict[str, list[str]] = {
        "GET": view_permissions,
        "OPTIONS": view_permissions,
        "HEAD": view_permissions,
        "POST": DjangoModelPermissions.perms_map["POST"],
        "PUT": DjangoModelPermissions.perms_map["PUT"],
        "PATCH": DjangoModelPermissions.perms_map["PATCH"],
        "DELETE": DjangoModelPermissions.perms_map["DELETE"],
    }


class AllowObjOwner(BasePermission):  # type: ignore[misc]
    def has_object_permission(
        self, request: HttpRequest, view: View, obj: models.Model
    ) -> bool:
        try:
            owner = obj.owner  # type: ignore[attr-defined]
        except AttributeError:
            owner = obj
        return owner == request.user


class IsSuperuserOrReadOnly(BasePermission):  # type: ignore[misc]
    def has_permission(self, request: HttpRequest, view: View) -> bool:
        if request.method in ["GET", "OPTIONS", "HEAD"]:
            return True
        return bool(
            request.user
            and request.user.is_superuser  # type: ignore[union-attr]
        )


def get_required_permissions(
    method: str, model: type[models.Model]
) -> list[str]:
    if method == "GET":
        return [f"{model._meta.app_label}.view_{model._meta.model_name}"]
    if method == "POST":
        return [f"{model._meta.app_label}.add_{model._meta.model_name}"]
    if method in ["PUT", "PATCH"]:
        return [f"{model._meta.app_label}.change_{model._meta.model_name}"]
    if method == "DELETE":
        return [f"{model._meta.app_label}.delete_{model._meta.model_name}"]
    return []
