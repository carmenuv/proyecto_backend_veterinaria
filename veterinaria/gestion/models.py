from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.db import models

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
  detalleDiagnostico = models.TextField(null=False, db_column='DetalleDiagnostico')
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

class AnalisisModel(models.Model):
  AnalisisID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreAnalisis = models.TextField(null=False, db_column='NombreAnalisis')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'analisis'

class TipoTrabajadorModel(models.Model):
  TipoTrabajadorID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreTrabajo = models.CharField(max_length=50, null= False, db_column='NombreTrabajo')
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipotrabajador'

class TipoProductoModel(models.Model):
  TipoProductoID = models.AutoField(primary_key=True, null=False, unique=True)
  nombreTipoProducto = models.CharField(max_length=250, null=False, db_column='NombreTipoProducto')
  descripcion = models.CharField(max_length=250, null=True, db_column='Descripcion')
  observacion = models.CharField(max_length=250, null=True, db_column='Observacion')

  class Meta:
    db_table = 'tipoproducto'


class AlmacenModel(models.Model):
  AlmacenID = models.AutoFiel(primary_key = True, null = False, unique = True)
  ProductoID = models.ForeignKey(ProductoModel, on_delete=models.CASCADE, db_column='ProductoID', null=False)
  Cantidad = models.FloatField(null=False)
  FechaIngreso = models.DateField(null=False)
  FechaVencimiento = models.DateField()
  observacion = models.TextField(null=True, db_column='Observacion')

  class Meta:
    db_table = 'almacen'

#dentro de ProductoModel
  def __str__(self):
    return self.Cantidad

class CitaModel(models.Model):
  CitasID = models.ForeignKey(ProductoModel, on_delete=models.CASCADE, db_column= 'ProductoID', null=False)
  AreatrabID = models.ForeignKey(AreaServicioModel, on_delete=models.CASCADE, db_column='AreaID', null= False)
  ClienteID = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, db_column='ClienteID', null=False)
  ServicioID = models.ForeignKey(ServicioModel, on_delete=models.CASCADE, db_column='ServicioID', null= False)
  PacienteID = models.ForeignKey(PacienteModel, on_delete=models.CASCADE, db_column='PacienteID', null=False)
    
  class Meta:
    db_table = 'citas'