from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthorOrReadOnly(BasePermission):
    def permission(self, request, view):
        return request.method in SAFE_METHODS and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS and request.user.is_authenticated or obj.author == request.user
