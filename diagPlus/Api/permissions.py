from rest_framework.permissions import BasePermission


class isAdminAuthenticated(BasePermission):
    # check if the user authenticated is an admin
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
