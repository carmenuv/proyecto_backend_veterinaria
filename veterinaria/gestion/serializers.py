
from rest_framework import serializers
from .models import EspecieModel,TipoDetalleAtencionModel,RazaModel, DiagnosticoModel, ServicioModel, AreaModel,TipoDocumentoModel, AnalisisModel, TipoTrabajadorModel, TipoProductoModel,ClienteModel,TrabajadorModel



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

# class IngresoPacienteNuevo(serializers.Serializer):
#   PacienteID = models.AutoField(primary_key= True, null=False, unique=True)
#   Raza = models.ForeignKey(TipoTrabajadorModel, on_delete=models.CASCADE, db_column='RazaID')
#   Cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, db_column='ClienteID')
#   Nombre = models.CharField(max_length=50, null=False, db_column='Nombre')
#   FechaNac = models.DateTimeField(auto_now_add=False, null=False, db_column='Nombre')
#   Sexo = models.CharField(max_length=50, null=False, choices=PETCHOICE,db_column='Sexo')
#   Peso = models.FloatField(null=False, db_column='Peso')
#   CodigoChip = models.CharField(max_length=100, null=False, db_column='CodigoChip')
#   Estado = models.CharField(max_length=50, null=False, choices=ESTADOCHOICE,db_column='Estado',default='HABILITADO')
#   observacion = models.TextField(null=True, db_column='Observacion')

class RegistrarUsuarioCliente(serializers.Serializer):
  