from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

#Usuairo anonimo
from django.contrib.auth.models import AnonymousUser

class PermisoAdmin(BasePermission):
    message = 'No tienes las credenciales necesarias para acceder a los recursos solicitados'

    def has_permission(self,request:Request,view):
        #si el metodo que esta utilizando es GET I OPTION I HEAD
        if request.method in SAFE_METHODS:            
            return True
        
        if isinstance(request.user, AnonymousUser):
            return False

        if request.user.tipoUsuario == 'ADMIN':
            return True
        
        else:
            return False


class PermisoMedico(BasePermission):
    message = 'No tienes las credenciales necesarias para acceder a los recursos solicitados'

    def has_permission(self,request:Request,view):
        #si el metodo que esta utilizando es GET I OPTION I HEAD
        if request.method in SAFE_METHODS:            
            return True
        
        if isinstance(request.user, AnonymousUser):
            return False

        if request.user.tipoUsuario == 'MEDICO':
            return True
        
        else:
            return False