from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
            # admin users only can see list view
        if request.user.is_staff:
            return True
        return False
    def has_object_permission(self, request, view, obj):

        if request.method == 'DELETE' and not request.user.is_staff:
            return False
        
        return obj.user == request.user or request.user.is_staff

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerAndReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to get a list and retrieve it.
    """

    def has_permission(self, request, view):
        # Allow listing if the action is 'list'
        if view.action == 'list':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Allow retrieval if the action is 'retrieve'
        if view.action == 'retrieve':
            return obj.owner == request.user
        return False