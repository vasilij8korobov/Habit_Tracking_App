from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Проверяет, является ли пользователь владельцем привычки.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешаем только владельцу объекта
        return obj.user == request.user
