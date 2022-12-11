from rest_framework import serializers
from .models import EspecieModel,TipoDetalleAtencionModel,RazaModel, DiagnosticoModel, ServicioModel

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
