from rest_framework.permissions import BasePermission

class IsAssignedUserOrReadOnly(BasePermission):
    """
    Custom permission to allow assigned users to view or edit the case,
    and restrict others to read-only access.
    """
    def has_object_permission(self, request, view, obj):
        # Safe methods (GET, HEAD, OPTIONS) are always allowed
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Write permissions are only allowed to the assigned user
        return obj.assigned_user == request.user
