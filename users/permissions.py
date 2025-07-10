from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """Только активные сотрудники имеют доступ к API"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active_employee
