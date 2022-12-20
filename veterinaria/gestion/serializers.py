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
      'NombreRaza': instance.NombreRaza,
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
