from django.db import models

class EspecieModel(models.Model):
  id = models.AutoField(primary_key= True, null=False, unique=True)
  nombreEspecie = models.CharField(max_length=50, null=False, db_column='nombre_especie')
  observacion = models.TextField

  class Meta:
    db_table = 'especie'