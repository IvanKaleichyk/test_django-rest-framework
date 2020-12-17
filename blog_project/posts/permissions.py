from rest_framework import permissions


class IsAuthOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class BasePermission(object):
    def has_permission(self, request, view):
        """
        Return true if permission is granted, False otherwise
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Return true if permission is granted, False otherwise
        """
        return True
