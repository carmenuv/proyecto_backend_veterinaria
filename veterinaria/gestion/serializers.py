from rest_framework import serializers
from .models import EspecieModel
from .models import AnalisisModel
from .models import TipoTrabajadorModels

class EspecieSerializer(serializers.ModelSerializer):
  class Meta:
    model = EspecieModel
    fields = '__all__'

class AnalisisSerializer(serializers.AnalisisModel):
  class Meta:
    model = AnalisisModel
    fields='__all__'

class TipoTrabajadorSerializer(serializers.TipoTrabajadorModels):
  class Meta:
    model = TipoTrabajadorModels
    fields = '__all__'
  