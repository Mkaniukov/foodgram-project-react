from rest_framework import permissions


class IsAuthorOnly(permissions.BasePermission):
    """
    Разрешение на изменение только для автора.
    Остальным только чтение объекта.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.method
            in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
