from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.db import models

class EspecieModel(models.Model):
  EspecieId = models.AutoField(primary_key= True, null=False, unique=True)
  nombreEspecie = models.CharField(max_length=50, null=False, db_column='NombreEspecie')
  observacion = models.TextField

  class Meta:
    db_table = 'especie'