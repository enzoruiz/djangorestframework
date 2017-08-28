from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'Debe haber creado esta pelicula para poder editarla.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
