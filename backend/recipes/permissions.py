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
        return (request.method in SAFE_METHODS
                or request.user and request.user.is_staff)
