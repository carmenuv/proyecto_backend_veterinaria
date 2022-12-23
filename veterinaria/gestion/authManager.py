from django.contrib.auth.models import BaseUserManager
# Manager > administrador que se encargara de la creacion del usuario por comando

class UsuarioManager(BaseUserManager):
    # Esta clase me servira para indicar como tenemos que crear el usuario cuando se haga por linea de comandos
    def create_superuser(self, correo, tipoUsuario, password):
        # Metodo que se mandara a llamar cuando se ejecute el comando 'createsuperuser'
        # los parametros que definimos en este metodo SE TIENE QUE LLAMAR IGUAL que los atributos del modelo
        if not correo: 
            raise ValueError('El usuario debe indicar obligatoriamente el correo')
        # normalizo el correo > aparte de validar el patron de correo lo que hace es remueve espacios en blanco innecesarios al inicio y al final y lo lleva todo a minuscula
        correoNormalizado = self.normalize_email(correo)
        nuevoUsuario = self.model(correo = correoNormalizado, tipoUsuario = tipoUsuario)
        nuevoUsuario.set_password(password)
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        nuevoUsuario.save(using=self._db)