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