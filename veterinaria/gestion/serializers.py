from rest_framework import serializers
from .models import EspecieModel,TipoDetalleAtencionModel,RazaModel, DiagnosticoModel, ServicioModel, AreaModel,TipoDocumentoModel, AnalisisModel, TipoTrabajadorModel, TipoProductoModel
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


#TipoUsuario
class TipoUsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    models = TipoUsuarioModel
    fields = '__all__'
#=================================================================================
#RECORDATORIO SERIALIZER
class RecordatorioSerializer(serializers.ModelSerializer):
  class Meta:
    models = RecordatorioModel
    fields = '__all__'

#RESULTADO SERIALIZER
class ResultadoSerializer(serializers.ModelSerializer):
  class Meta:
    models = ResultadoModel
    fields = '__all__'