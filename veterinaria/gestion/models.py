
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.db import models


ESTADOCHOICE = (
    ('1', 'HABILITADO'),
    ('2', 'DESHABILITADO')
)


PETCHOICE = (
    ('1', 'MACHO'),
    ('2', 'HEMBRA')
)

class TipoUsuarioModel(models.Model):
  TipoUsuarioID = models.AutoField(primary_key=True, null= False, unique=True, db_column='TipoUsuarioID')
  Descripcion = models.CharField(max_length=50, null=False, db_column='Descripcion')
  Observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'TipoUsuario'
  def __str__(self):
    return self.Descripcion

class UsuarioModel(models.Model):
  UsuarioID = models.AutoField(primary_key= True, null=False, unique=True)
  TipoUsuario = models.ForeignKey(TipoUsuarioModel, on_delete=models.CASCADE, db_column='TipoUsuarioID')
  Alias = models.CharField(max_length=50, null=False, db_column='Alias')
  Password = models.TextField(null=True, db_column='Password')
  Correo = models.EmailField(max_length=250, null=False, db_column='Correo')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Usuario'


class EspecieModel(models.Model):
  EspecieID = models.AutoField(primary_key= True, null=False, unique=True)
  nombreEspecie = models.CharField(max_length=50, null=False, db_column='NombreEspecie')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'especie'

  def __str__(self):
    return self.nombreEspecie

class TipoDetalleAtencionModel(models.Model):
  TipoDetalleAtencionID = models.AutoField(primary_key= True, null=False, unique=True)
  NombreDetalle = models.CharField(max_length=100, null=False, db_column='NombreDetalle')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipodetalleatencion'

class RazaModel(models.Model):
  RazaID = models.AutoField(primary_key= True, null=False, unique=True)
  Especie = models.ForeignKey(EspecieModel, on_delete=models.CASCADE, db_column='EspecieID')
  NombreRaza = models.CharField(max_length=50, null=False, db_column='NombreRaza')
  Observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Raza'

class DiagnosticoModel(models.Model):
  DiagnosticoID = models.AutoField(primary_key=True, null=False, unique=True)
  detalleDiagnostico = models.TextField(max_length=50,null=False, db_column='DetalleDiagnostico')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'diagnostico'

class ServicioModel(models.Model):
  ServicioID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreServicio = models.CharField(max_length=100, null=False, db_column='NombreServicio')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'servicio'

class AreaModel(models.Model):
  AreaID = models.AutoField(primary_key= True, null=False, unique=True)
  nombreArea = models.CharField(max_length=100, null=False, db_column='NombreArea')
  Descripcion = models.CharField(max_length=250, null=False, db_column='Descripcion')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'area'

class TipoDocumentoModel(models.Model):
  TipoDocumentoID = models.AutoField(primary_key= True, null=False, unique=True)
  nombreDocumento = models.CharField(max_length=50, null=False, db_column='NombreDocumento')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipodocumento'
  def __str__(self):
    return self.nombreDocumento

class AnalisisModel(models.Model):
  AnalisisID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreAnalisis = models.TextField(max_length=100,null=False, db_column='NombreAnalisis')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'analisis'

class TipoTrabajadorModel(models.Model):
  TipoTrabajadorID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreTrabajo = models.CharField(max_length=50, null= False, db_column='NombreTrabajo')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipotrabajador'
  def __str__(self):
    return self.nombreTrabajo


class TipoProductoModel(models.Model):
  TipoProductoID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreTipoProducto = models.CharField(max_length=100, null=False, db_column='NombreTipoProducto')
  descripcion = models.CharField(max_length=250, null=True, db_column='Descripcion')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipoproducto'


class ClienteModel(models.Model):
  ClienteID = models.AutoField(primary_key= True, null=False, unique=True)
  TipoDocumento = models.ForeignKey(TipoDocumentoModel, on_delete=models.CASCADE, db_column='TipoDocumentoID')
  Usuario = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE, db_column='UsuarioID')
  Documento = models.CharField(max_length=15, null=False, db_column='Documento',unique=True)
  Nombre = models.CharField(max_length=250, null=False, db_column='Nombre')
  ApePaterno = models.CharField(max_length=100, null=False, db_column='ApePaterno')
  ApeMaterno = models.CharField(max_length=100, null=False, db_column='ApeMaterno')
  NroContacto = models.CharField(max_length=12, null=False, db_column='NroContacto')
  NroAuxiliar = models.CharField(max_length=12, null=True, db_column='NroAuxiliar')
  Direccion = models.CharField(max_length=250, null=False, db_column='Direccion')
  Correo = models.EmailField(max_length=250, null=False, db_column='Correo')
  Estado = models.CharField(max_length=50, null=False, choices=ESTADOCHOICE,db_column='Estado',default='HABILITADO')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Cliente'

class TrabajadorModel(models.Model):
  TrabajadorID = models.AutoField(primary_key= True, null=False, unique=True)
  TipoTrabajador = models.ForeignKey(TipoTrabajadorModel, on_delete=models.CASCADE, db_column='TipoTrabajadorID')
  TipoDocumento = models.ForeignKey(TipoDocumentoModel, on_delete=models.CASCADE, db_column='TipoDocumentoID')
  Usuario = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE, db_column='UsuarioID')
  Documento = models.CharField(max_length=15, null=False, db_column='Documento',unique=True)
  Nombre = models.CharField(max_length=250, null=False, db_column='Nombre')
  ApePaterno = models.CharField(max_length=100, null=False, db_column='ApePaterno')
  ApeMaterno = models.CharField(max_length=100, null=False, db_column='ApeMaterno')
  NroContacto = models.CharField(max_length=12, null=False, db_column='NroContacto')
  NroAuxiliar = models.CharField(max_length=12, null=True, db_column='NroAuxiliar')
  Direccion = models.CharField(max_length=250, null=False, db_column='Direccion')
  Correo = models.EmailField(max_length=250, null=False, db_column='Correo')
  Estado = models.CharField(max_length=50, null=False, choices=ESTADOCHOICE,db_column='Estado',default='HABILITADO')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Trabajador'

class PacienteModel(models.Model):
  PacienteID = models.AutoField(primary_key= True, null=False, unique=True)
  Raza = models.ForeignKey(TipoTrabajadorModel, on_delete=models.CASCADE, db_column='RazaID')
  Cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, db_column='ClienteID')
  Nombre = models.CharField(max_length=50, null=False, db_column='Nombre')
  FechaNac = models.DateTimeField(auto_now_add=False, null=False, db_column='FechaNac')
  Sexo = models.CharField(max_length=50, null=False, choices=PETCHOICE,db_column='Sexo')
  Peso = models.FloatField(null=False, db_column='Peso')
  CodigoChip = models.CharField(max_length=100, null=False, db_column='CodigoChip')
  Estado = models.CharField(max_length=50, null=False, choices=ESTADOCHOICE,db_column='Estado',default='HABILITADO')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Paciente'

class HClinicaModel(models.Model):
  HClinicaID = models.AutoField(primary_key= True, null=False, unique=True)
  Cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, db_column='ClienteID')
  PacienteID = models.ForeignKey(PacienteModel, on_delete=models.CASCADE, db_column='PacienteID')
  FechaApertura = models.DateTimeField(auto_now_add=True, null=False, db_column='FechaApertura')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'HIstoria_clinica'




