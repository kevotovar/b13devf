from rest_framework import permissions

class GroupPermission(permissions.BasePermission):
    message = "Usted no puede acceder"
    SELECTED_GROUP = 'Writers'

    def has_permission(self, request, view):
        
        if request.user.groups.filter(name=self.SELECTED_GROUP):
            return True
        else:
            return False