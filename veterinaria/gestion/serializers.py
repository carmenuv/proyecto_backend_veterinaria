from rest_framework import serializers
from .models import EspecieModel

class EspecieSerializer(serializers.ModelSerializer):
  class Meta:
    model = EspecieModel
    fields = '__all__'