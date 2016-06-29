from rest_framework.permissions import BasePermission

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class CardCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_company or request.method in SAFE_METHODS


class CardAccessPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_company:
            if request.user.company != obj.company or not request.method in SAFE_METHODS:
                return False
        else:
            return request.user.profile == obj.profile


class AddressCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_company or request.method in SAFE_METHODS


class AddressAccessPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_company and request.user.company == obj.company
