from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmployerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or request.user
            and request.user_is_authenticated
            and obj.employer == request.user
        )
