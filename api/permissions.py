from rest_framework.permissions import BasePermission

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class CardAccessPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_company or request.method in SAFE_METHODS:
            return True
        return False
