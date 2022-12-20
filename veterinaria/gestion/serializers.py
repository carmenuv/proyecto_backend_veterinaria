from rest_framework import serializers
from .models import *

class EspecieSerializer(serializers.ModelSerializer):
  class Meta:
    model = EspecieModel
    fields = '__all__'

class TipoDetalleAtencionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoDetalleAtencionModel
    fields = '__all__'

class RazaSerializer(serializers.ModelSerializer):

  class Meta:
    model = RazaModel
    fields = ('RazaID','Especie','NombreRaza','Observacion')

  def to_representation(self, instance):
      return {
        'RazaID': instance.RazaID,
        'Especie' : instance.Especie.nombreEspecie,
        'Nombre': instance.NombreRaza,
        'Observacion' : instance.Observacion,
    }

class Raza2Serializer(serializers.ModelSerializer):

  class Meta:
    model = RazaModel
    fields = ('RazaID','Especie','NombreRaza','Observacion')

class DiagnosticoSerializer(serializers.ModelSerializer):
  class Meta:
    model = DiagnosticoModel
    fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServicioModel
    fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
  class Meta:
    model = AreaModel
    fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoDocumentoModel
    fields = '__all__'

class AnalisisSerializer(serializers.ModelSerializer):
  class Meta:
    model = AnalisisModel
    fields='__all__'

class TipoTrabajadorSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoTrabajadorModel
    fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoProductoModel
    fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductoModel
    fields = ('ProductoID','TipoProducto','NombreProducto','Descripcion', 'PrecioUnitario', 'Observacion')

  def to_representation(self, instance):
    return {
      'ProductoID': instance.ProductoID,
      'TipoProducto' : instance.TipoProducto.Tipoproducto,
      'NombreProducto': instance.NombreProducto,
      'Descripcion' : instance.Descipcion,
      'PrecioUnitario' : instance.PrecioUnitario,
      'Observacion' : instance.Observacion,
    }

class Producto2Serializer(serializers.ModelSerializer):
  class Meta:
    model = ProductoModel
    fields = ('ProductoID','TipoProducto','NombreProducto','Descripcion', 'PrecioUnitario', 'Observacion')

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClienteModel
    fields = '__all__'
    extra_kwargs = {
              'Estado': {
                  'read_only': True
              }
          }

  def to_representation(self, instance):
      return {
        'ID': instance.ClienteID,
        'Tipo de Documento' : instance.TipoDocumento.nombreDocumento,
        'Documento': instance.Documento,
        'Nombre Cliente': instance.Nombre,
        'Apellido Paterno': instance.ApePaterno,
        'Apellido Materno': instance.ApeMaterno,
        'NroContacto': instance.NroContacto,
        'NroAuxiliar': instance.NroAuxiliar,
        'Direccion': instance.Direccion,
        'E-mail': instance.Correo,
        'Estado': instance.Estado,
        'Observacion' : instance.observacion,
    }

class Cliente2Serializer(serializers.ModelSerializer):
  class Meta:
    model = ClienteModel
    fields = '__all__'
    extra_kwargs = {
            'Estado': {
                'read_only': True
            }
        }

class TrabajadorSerializer(serializers.ModelSerializer):
  class Meta:
    model = TrabajadorModel
    fields = '__all__'
    extra_kwargs = {
              'Estado': {
                  'read_only': True
              }
          }

  def to_representation(self, instance):
      return {
        'ID': instance.TrabajadorID,
        'Tipo de Trabajador' : instance.TipoTrabajador.nombreTrabajo,
        'Tipo de Documento' : instance.TipoDocumento.nombreDocumento,
        'Documento': instance.Documento,
        'Nombre Cliente': instance.Nombre,
        'Apellido Paterno': instance.ApePaterno,
        'Apellido Materno': instance.ApeMaterno,
        'NroContacto': instance.NroContacto,
        'NroAuxiliar': instance.NroAuxiliar,
        'Direccion': instance.Direccion,
        'E-mail': instance.Correo,
        'Estado': instance.Estado,
        'Observacion' : instance.observacion,
    }

class Trabajador2Serializer(serializers.ModelSerializer):
  class Meta:
    model = TrabajadorModel
    fields = '__all__'
    extra_kwargs = {
              'Estado': {
                  'read_only': True
              }
          }

class AlmacenSerializer(serializers.ModelSerializer):
  class Meta:
    model = AlmacenModel
    fields = ('AlmacenID','ProductoID','Cantidad','FechaIngreso', 'FechaVencimiento', 'Observacion')

  def to_representation(self, instance):
    return {
      'AlmacenID': instance.AlmacenID,
      'ProductoID' : instance.ProductoID,
      'Cantidad': instance.Cantidad,
      'FechaIngreso' : instance.FechaIngreso,
      'FechaVencimiento' : instance.FechaVencimiento,
      'Observacion' : instance.Observacion,
    }

class Almacen2Serializer(serializers.ModelSerializer):
  class Meta:
    model = AlmacenModel
    fields = ('AlmacenID','ProductoID','Cantidad','FechaIngreso', 'FechaVencimiento', 'Observacion')


class CitaSerializer(serializers.ModelSerializer):
  class Meta:
    model = CitaModel
    fields = ('CitasID','AreatrabID','ClienteID','ServicioID', 'PacienteID')

  def to_representation(self, instance):
    return {
      'CitasID': instance.AlmacenID,
      'AreatrabID' : instance.ProductoID,
      'ClienteID': instance.Cantidad,
      'ServicioID' : instance.FechaIngreso,
      'PacienteID' : instance.FechaVencimiento,
      
    }

class Cita2Serializer(serializers.ModelSerializer):
  class Meta:
    model = CitaModel
    fields = ('CitasID','AreatrabID','ClienteID','ServicioID', 'PacienteID')