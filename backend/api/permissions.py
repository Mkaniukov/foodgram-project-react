from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешение на создание и изменение только для пользователя.
    Остальным только чтение объекта.
    """
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    """
    Разрешение на создание и изменение только для админов.
    Остальным только чтение объекта.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method in permissions.SAFE_METHODS
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return request.method in permissions.SAFE_METHODS
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)


class IsAuthorOnly(permissions.BasePermission):
    """
    Разрешение на изменение только для автора.
    Остальным только чтение объекта.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and (
                request.user.is_admin
                or obj.author == request.user or request.method == 'POST'):
            return True
        return request.method in permissions.SAFE_METHODS
