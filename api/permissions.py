from rest_framework.permissions import BasePermission


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
