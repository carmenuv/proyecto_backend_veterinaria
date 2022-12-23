
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from .authManager import UsuarioManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

ESTADOCHOICE = (
    ('1', 'HABILITADO'),
    ('2', 'DESHABILITADO')
)


PETCHOICE = (
    ('1', 'MACHO'),
    ('2', 'HEMBRA')
)

VENTACHOICE = (
    ('1', 'GENERADA'),
    ('2', 'EN PREPARACION'),
    ('3', 'PENDIENTE'),
    ('4', 'ENVIADA'),
    ('5', 'ENTREGADA'),
)

USERCHOICE = (
    ('ADMIN', 'ADMINISTRADOR'), 
    ('MEDICO', 'MEDICO'),
    ('GROOMER', 'GROOMER'),
    ('ASISTENTE MEDICO', 'ASISTENTE MEDICO'),
    ('ASISTENTE ADMINISTRATIVO', 'ASISTENTE ADMINISTRATIVO'),
    ('VENDEDOR', 'VENDEDOR'),
    ('CLIENTE', 'CLIENTE')
)

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
  id = models.AutoField(primary_key= True, null=False, unique=True)
  TipoUsuario = models.CharField(max_length=40, choices= USERCHOICE, db_column='TipoUsuario')
  password = models.TextField(null=False, db_column='password')
  Correo = models.EmailField(max_length=250, null=False, db_column='Correo',unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  objects = UsuarioManager()

  USERNAME_FIELD = 'Correo'
  REQUIRED_FIELDS = ['tipoUsuario']

  class Meta:
    db_table = 'Usuario'

class EspecieModel(models.Model):
  EspecieID = models.AutoField(primary_key= True, null=False, unique=True)
  nombreEspecie = models.CharField(max_length=50, null=False, db_column='NombreEspecie',unique=True)
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'especie'

  def __str__(self):
    return self.nombreEspecie

class TipoDetalleAtencionModel(models.Model):
  TipoDetalleAtencionID = models.AutoField(primary_key= True, null=False, unique=True)
  NombreDetalle = models.CharField(max_length=100, null=False,unique=True, db_column='NombreDetalle')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipodetalleatencion'

class RazaModel(models.Model):
  RazaID = models.AutoField(primary_key= True, null=False, unique=True)
  Especie = models.ForeignKey(EspecieModel, on_delete=models.CASCADE, db_column='EspecieID')
  NombreRaza = models.CharField(max_length=50, null=False, db_column='NombreRaza',unique=True)
  Observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Raza'
  def __str__(self):
    return self.NombreRaza

class DiagnosticoModel(models.Model):
  DiagnosticoID = models.AutoField(primary_key=True, null=False, unique=True)
  detalleDiagnostico = models.CharField(max_length=50,unique=True, null=False, db_column='DetalleDiagnostico')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'diagnostico'

class ServicioModel(models.Model):
  ServicioID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreServicio = models.CharField(max_length=100,unique=True, null=False, db_column='NombreServicio')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'servicio'

class AreaModel(models.Model):
  AreaID = models.AutoField(primary_key= True, null=False, unique=True)
  nombreArea = models.CharField(max_length=100,unique=True, null=False, db_column='NombreArea')
  Descripcion = models.CharField(max_length=250, null=False, db_column='Descripcion')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'area'

class TipoDocumentoModel(models.Model):
  TipoDocumentoID = models.AutoField(primary_key= True, null=False, unique=True)
  nombreDocumento = models.CharField(max_length=50,unique=True, null=False, db_column='NombreDocumento')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipodocumento'
  def __str__(self):
    return self.nombreDocumento

class AnalisisModel(models.Model):
  AnalisisID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreAnalisis = models.CharField(max_length=100,unique=True, null=False, db_column='NombreAnalisis')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'analisis'

class TipoTrabajadorModel(models.Model):
  TipoTrabajadorID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreTrabajo = models.CharField(max_length=50,unique=True, null= False, db_column='NombreTrabajo')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipotrabajador'
  def __str__(self):
    return self.nombreTrabajo


class TipoProductoModel(models.Model):
  TipoProductoID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreTipoProducto = models.CharField(max_length=100,unique=True, null=False, db_column='NombreTipoProducto')
  descripcion = models.CharField(max_length=250, null=True, db_column='Descripcion')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipoproducto'
  def __str__(self):
    return self.nombreTipoProducto

class ProductoModel(models.Model):
  ProductoID = models.AutoField(primary_key= True, null=False, unique=True)
  TipoProducto = models.ForeignKey(TipoProductoModel, on_delete=models.CASCADE, db_column='TipoproductoID')
  NombreProducto = models.CharField(max_length=250,unique=True, null=False, db_column='NombreProducto')
  Descripcion = models.CharField(max_length=250, null=True, db_column='Descripcion')
  PrecioUnitario = models.FloatField(null=False, db_column='PrecioUnitario')
  Observacion = models.CharField(max_length=250, null=True, db_column='Observacion')

  class Meta:
    db_table = 'producto'


class ClienteModel(models.Model):
  ClienteID = models.AutoField(primary_key= True, null=False, unique=True)
  TipoDocumento = models.ForeignKey(TipoDocumentoModel, on_delete=models.CASCADE, db_column='TipoDocumentoID')
  Documento = models.CharField(max_length=15,unique=True, null=False, db_column='Documento')
  Nombre = models.CharField(max_length=250, null=False, db_column='Nombre')
  ApePaterno = models.CharField(max_length=100, null=False, db_column='ApePaterno')
  ApeMaterno = models.CharField(max_length=100, null=False, db_column='ApeMaterno')
  NroContacto = models.CharField(max_length=12, null=False, db_column='NroContacto')
  NroAuxiliar = models.CharField(max_length=12, null=True, db_column='NroAuxiliar')
  Direccion = models.CharField(max_length=250, null=False, db_column='Direccion')
  Correo = models.EmailField(max_length=250,unique=True, null=False, db_column='Correo')
  Estado = models.CharField(max_length=50, null=False, choices=ESTADOCHOICE,db_column='Estado',default='HABILITADO')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Cliente'
  
  def __str__(self):
    return (self.Nombre+" "+self.ApePaterno+" "+self.ApeMaterno)

class TrabajadorModel(models.Model):
  TrabajadorID = models.AutoField(primary_key= True, null=False, unique=True)
  TipoTrabajador = models.ForeignKey(TipoTrabajadorModel, on_delete=models.CASCADE, db_column='TipoTrabajadorID')
  TipoDocumento = models.ForeignKey(TipoDocumentoModel, on_delete=models.CASCADE, db_column='TipoDocumentoID')
  Documento = models.CharField(max_length=15,unique=True, null=False, db_column='Documento')
  Nombre = models.CharField(max_length=250, null=False, db_column='Nombre')
  ApePaterno = models.CharField(max_length=100, null=False, db_column='ApePaterno')
  ApeMaterno = models.CharField(max_length=100, null=False, db_column='ApeMaterno')
  NroContacto = models.CharField(max_length=12, null=False, db_column='NroContacto')
  NroAuxiliar = models.CharField(max_length=12, null=True, db_column='NroAuxiliar')
  Direccion = models.CharField(max_length=250, null=False, db_column='Direccion')
  Correo = models.EmailField(max_length=250,unique=True, null=False, db_column='Correo')
  Estado = models.CharField(max_length=50, null=False, choices=ESTADOCHOICE,db_column='Estado',default='HABILITADO')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'Trabajador'

class servicioTrabajadorModel(models.Model):
  SerTrabID = models.AutoField(primary_key=True, null=False, unique=True)
  Servicio = models.ForeignKey(ServicioModel, on_delete=models.CASCADE, db_column='ServicioID')
  Trabajador = models.ForeignKey(TrabajadorModel, on_delete=models.CASCADE, db_column='TrabajadorID')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'servicioTrabajador'
    unique_together = ('Servicio', 'Trabajador')

  def __str__(self):
    return(self.Servicio.nombreServicio+" "+self.Trabajador.ApePaterno +" "+self.Trabajador.ApeMaterno)

class PacienteModel(models.Model):
  PacienteID = models.AutoField(primary_key= True, null=False, unique=True)
  Raza = models.ForeignKey(RazaModel, on_delete=models.CASCADE, db_column='RazaID')
  Cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, db_column='ClienteID')
  Nombre = models.CharField(max_length=50, null=False, db_column='Nombre')
  FechaNac = models.DateTimeField(auto_now_add=False, null=False, db_column='FechaNac')
  Sexo = models.CharField(max_length=50, null=False, choices=PETCHOICE,db_column='Sexo')
  Peso = models.FloatField(null=False, db_column='Peso')
  CodigoChip = models.CharField(max_length=100, null=False, db_column='CodigoChip')
  Foto = models.ImageField(null=True,blank='',default='',upload_to='fotospet/',db_column='Foto')
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
    unique_together = ('Cliente', 'PacienteID')

class AreaServicioModel(models.Model):
  AreaTrabID = models.AutoField(primary_key= True, null=False, unique=True)
  Area = models.ForeignKey(AreaModel, on_delete=models.CASCADE, db_column='AreaID')
  ServTrab = models.ForeignKey(servicioTrabajadorModel, on_delete=models.CASCADE, db_column='ServTrabID')
  Fecha = models.DateField(auto_now_add=False, null=False, db_column='fecha')
  horaInicio = models.DateTimeField(null=False, db_column='horainicio')
  horaFin = models.DateTimeField(null=False, db_column='horafin')
  cupo = models.IntegerField(null=False, db_column='Cupo')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'areaServicio'
    unique_together = ('Area', 'ServTrab')

class AlmacenModel(models.Model):
  AlmacenID = models.AutoField(primary_key = True, null = False, unique = True)
  Producto = models.ForeignKey(ProductoModel, on_delete=models.CASCADE, db_column='ProductoID', null=False,unique=True)
  Cantidad = models.FloatField(null=False, db_column='Cantidad')
  FechaIngreso = models.DateField(null=False, db_column='FechaIngreso')
  FechaVencimiento = models.DateField(null=True,blank=False, db_column='FechaVencimiento')
  observacion = models.TextField(null=True, db_column='observacion')

  class Meta:
    db_table = 'almacen'

  def __str__(self):
    return self.Cantidad
    
class CitaModel(models.Model):
  CitasID = models.AutoField(primary_key = True, null = False, unique = True)
  AreatrabID = models.ForeignKey(AreaServicioModel, on_delete=models.CASCADE, db_column='AreaID', null= False)
  ClienteID = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, db_column='ClienteID', null=False)
  ServicioID = models.ForeignKey(ServicioModel, on_delete=models.CASCADE, db_column='ServicioID', null= False)
  PacienteID = models.ForeignKey(PacienteModel, on_delete=models.CASCADE, db_column='PacienteID', null=False)
    
  class Meta:
    db_table = 'citas'
    unique_together = ('AreatrabID', 'ClienteID', 'ServicioID', 'PacienteID'),

class VentaModel(models.Model):
  VentaID = models.AutoField(primary_key = True, null = False, unique = True)
  Cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, db_column='ClienteID')
  Fecha = models.DateTimeField(auto_now_add=True, null=False, db_column='Fecha')
  Estado = models.CharField(max_length=50, null=False, choices=VENTACHOICE,db_column='Estado',default='GENERADA')
  Direccion = models.CharField(max_length=250, null=False, db_column='Direccion', default='ENTREGA EN TIENDA')
  MontoT = models.FloatField(null=False, db_column='MontoT', default=0)
  Descuento = models.FloatField(null=True, db_column='Descuento', default=0)
  Observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'venta'

class DetalleVentaModel(models.Model):
  DetalleVentaID = models.AutoField(primary_key = True, null = False, unique = True)
  VentaID = models.ForeignKey(VentaModel, on_delete=models.CASCADE, db_column='VentaID')
  Producto = models.ForeignKey(ProductoModel, on_delete=models.CASCADE, db_column='ProductoID')
  Cantidad = models.FloatField(null=False, db_column='Cantidad', default=0)
  MontoD = models.FloatField(null=False, db_column='MontoD', default=0)

  class Meta:
    db_table = 'detalleventa'
    unique_together = ('VentaID', 'Producto')

class AtencionModel(models.Model):
  AtencionID = models.AutoField(primary_key = True, null = False, unique = True)
  HClinica = models.ForeignKey(HClinicaModel, on_delete=models.CASCADE, db_column='HClinicaID')
  AreatrabID = models.ForeignKey(AreaServicioModel, on_delete=models.CASCADE, db_column='AreaID')
  ServicioID = models.ForeignKey(ServicioModel, on_delete=models.CASCADE, db_column='ServicioID')
  Trabajador = models.ForeignKey(TrabajadorModel, on_delete=models.CASCADE, db_column='TrabajadorID')
  DiagnosticoID = models.ForeignKey(DiagnosticoModel, on_delete=models.CASCADE, db_column='DiagnosticoID')
  FechaAtencion = models.DateTimeField(auto_now_add=True, null=False, db_column='FechaAtencion')
  SiguienteAtencion = models.DateTimeField(auto_now_add=False, null=False, db_column='SiguienteAtencion')
  MontoT = models.FloatField(null=False, db_column='MontoT', default=0)
  Observacion = models.TextField(null=False, db_column='Observacion')

  class Meta:
    db_table = 'atencion'


class DetalleAtencionModel(models.Model):
  DetalleAtencionID = models.AutoField(primary_key=True, unique=True, null=False)
  AtencionID = models.ForeignKey(AtencionModel, on_delete=models.CASCADE, db_column='AtencionID', null= False)
  TipoDetalleAtencionID = models.ForeignKey(TipoDetalleAtencionModel, on_delete=models.CASCADE, db_column='TipodetalleAtencionID', null= False)
  Precio = models.FloatField(null=False, db_column='precio')
  Cantidad = models.FloatField(null=False, db_column='Cantidad')
  Descuento = models.FloatField(null=False, db_column='descuento')
  MontoD = models.FloatField(null=False, db_column='MontoD', default=0)
  Observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'detalleatencion'
    unique_together = ('TipoDetalleAtencionID', 'AtencionID')

class OrdenLaboratorioModel(models.Model):
  OrdenlabID = models.AutoField(primary_key = True, null = False, unique = True)
  AtencionID = models.ForeignKey(AtencionModel, on_delete=models.CASCADE, db_column='AtencionID')
  Trabajador = models.ForeignKey(TrabajadorModel, on_delete=models.CASCADE, db_column='TrabajadorID')
  Fecha = models.DateTimeField(auto_now_add=True, null=False, db_column='Fecha')
  Observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'ordenlaboratorio'

class RecordatorioModel(models.Model):
  RecordatorioID = models.AutoField(primary_key = True, null = False, unique = True)
  AtencionID = models.ForeignKey(AtencionModel, on_delete=models.CASCADE, db_column='AtencionID')
  ServicioID = models.ForeignKey(ServicioModel, on_delete=models.CASCADE, db_column='ServicioID')
  PacienteID = models.ForeignKey(PacienteModel, on_delete=models.CASCADE, db_column='PacienteID')
  FechaRecordatorio = models.DateTimeField(auto_now_add=True, null=False, db_column='FechaRecordatorio')

  class Meta:
    db_table = 'recordatorio'

class DetalleOrdenAnalisisModel(models.Model):
  DetalleOrdenID = models.AutoField(primary_key = True, null = False, unique = True)
  OrdenLabID = models.ForeignKey(OrdenLaboratorioModel, on_delete=models.CASCADE, db_column='OrdenLabID')
  AnalisisID = models.ForeignKey(AnalisisModel, on_delete=models.CASCADE, db_column='AnalisisID')
  Precio = models.FloatField(null=False, db_column='Precio')
  Descuento = models.FloatField(null=False, db_column='Descuento')
  Observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'detalleordenanalisis'
    unique_together = ('OrdenLabID','AnalisisID')

class ResultadoModel(models.Model):
  ResultadoID = models.AutoField(primary_key=True, unique=True, null=False)
  DetalleOrdenID = models.ForeignKey(DetalleOrdenAnalisisModel, on_delete=models.CASCADE, db_column='DetalleOrdenID', null= False)
  DescripcionResultado = models.CharField(max_length=45, null=False, db_column='DescripcionResultado')
  Fecha = models.DateField(null=False, db_column='Fecha')
  Observacion = models.CharField(max_length=250, null=True, db_column='Observacion')
  Indicacion = models.CharField(max_length=250, null=True, db_column='Indicacion')

  class Meta:
    db_table = 'resultado'


