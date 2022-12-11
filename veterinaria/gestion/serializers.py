from rest_framework import serializers
from .models import EspecieModel
from .models import AnalisisModel
from .models import TipoTrabajadorModel

class EspecieSerializer(serializers.ModelSerializer):
  class Meta:
    model = EspecieModel
    fields = '__all__'

class AnalisisSerializer(serializers.AnalisisModel):
  class Meta:
    model = AnalisisModel
    fields='__all__'

class TipoTrabajadorSerializer(serializers.TipoTrabajadorModel):
  class Meta:
    model = TipoTrabajadorModel
    fields = '__all__'
  