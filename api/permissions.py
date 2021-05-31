from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsSuperuserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or
            request.user.is_staff
            or
            request.user.is_superuser
        )
