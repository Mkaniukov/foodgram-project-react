from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework import permissions


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user and request.user.is_staff)


class IsAuthorOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.method
                in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
