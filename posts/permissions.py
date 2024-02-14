from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read permissions re allowed to any reqeust so we will always
        #allow GET, HEAD, or OPTIONS reqeuests
        if request.method in permissions.SAFE_METHODS:
            return True
        #Write permissions are only allowed to the author of a post
        return obj.author ==request.user