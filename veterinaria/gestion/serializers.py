
from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    models = UsuarioModel
    fields = '__all__'

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
    fields = ('TipoProductoID','nombreTipoProducto','descripcion','observacion')

  def to_representation(self, instance):
    return {
      'TipoProductoID': instance.TipoProductoID,
      'nombreTipoProducto' : instance.nombreTipoProducto,
      'descripcion': instance.descripcion,
      'observacion' : instance.observacion
    }

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductoModel
    fields = ('ProductoID','TipoProducto','NombreProducto','Descripcion', 'PrecioUnitario', 'Observacion')

class Producto2Serializer(serializers.ModelSerializer):
  class Meta:
    model = ProductoModel
    fields = ('ProductoID','TipoProducto','NombreProducto','Descripcion', 'PrecioUnitario', 'Observacion')

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



class servicioTrabajadorSerializer(serializers.ModelSerializer):

  class Meta:

    model = servicioTrabajadorModel
    fields = ('SerTrabID','Servicio','Trabajador','observacion')
    
  def to_representation(self, instance):
    return {
      'SerTrabID': instance.SerTrabID,
      'Servicio' : instance.Servicio.nombreServicio,
      'Trabajador': instance.Trabajador.ApePaterno+' '+instance.Trabajador.ApeMaterno+' '+instance.Trabajador.Nombre,
      'observacion' : instance.observacion,
    }

class servicioTrabajador2Serializer(serializers.ModelSerializer):
  class Meta:
    model = servicioTrabajadorModel
    fields = '__all__'
    extra_kwargs = {
              'Estado': {
                  'read_only': True
              }
          }


class areaServicioSerializer(serializers.ModelSerializer):

  class Meta:

    model = AreaServicioModel
    fields = ('AreaTrabID','Area','ServTrab','Fecha','horaInicio','horaFin','cupo','observacion')
    
  def to_representation(self, instance):
    return {
      'AreaTrabID': instance.AreaTrabID,
      'Area' : instance.Area.nombreArea,
      'Servicio Trabajador':  instance.ServTrab.Servicio.nombreServicio+' - '+instance.ServTrab.Trabajador.Nombre+' '+instance.ServTrab.Trabajador.ApePaterno+' '+instance.ServTrab.Trabajador.ApeMaterno,
      'Fecha' : instance.Fecha,
      'horaInicio' : instance.horaInicio.strftime('%H:%M'),
      'horaFin' : instance.horaFin.strftime('%H:%M'),
      'cupo' : instance.cupo,
      'observacion' : instance.observacion,
    }

    

class areaServicio2Serializer(serializers.ModelSerializer):
  class Meta:
    model = AreaServicioModel
    fields = '__all__'
    

class AlmacenSerializer(serializers.ModelSerializer):
  class Meta:
    model = AlmacenModel
    fields = ('AlmacenID','Producto','Cantidad','FechaIngreso', 'FechaVencimiento', 'observacion')

  def to_representation(self, instance):
    return {
      'AlmacenID': instance.AlmacenID,
      'Producto' : instance.Producto.NombreProducto,
      'Cantidad': instance.Cantidad,
      'FechaIngreso' : instance.FechaIngreso,
      'FechaVencimiento' : instance.FechaVencimiento,
      'Observacion' : instance.observacion,
    }

class Almacen2Serializer(serializers.ModelSerializer):
  class Meta:
    model = AlmacenModel
    fields = ('AlmacenID','Producto','Cantidad','FechaIngreso', 'FechaVencimiento', 'observacion')


class CitaSerializer(serializers.ModelSerializer):
  class Meta:
    model = CitaModel
    fields = ('CitasID','Areatrab','Cliente','Servicio', 'Paciente')

  def to_representation(self, instance):
    return {
      'CitasID': instance.CitasID,
      'Areatrab' : instance.AreatrabID.Area,
      'Cliente': instance.ClienteID.Nombre,
      'Servicio' : instance.ServicioID.nombreServicio,
      'Paciente' : instance.PacienteID.Nombre,
    }

class Cita2Serializer(serializers.ModelSerializer):
  class Meta:
    model = CitaModel
    fields = ('CitasID','Areatrab','Cliente','Servicio', 'Paciente')


class VentaSerializer(serializers.ModelSerializer):
  class Meta:
    model = VentaModel
    fields = '__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
  class Meta:
    model = DetalleOrdenAnalisisModel
    fields = '__all__'

class AtencionSerializer(serializers.ModelSerializer):
  class Meta:
    model = AtencionModel
    fields = '__all__'

class DetalleAtencionClinicaSerializer(serializers.ModelSerializer):
  class Meta:
    model = DetalleAtencionClinicaModel
    fields = '__all__'

class DetalleAtencionServicioSerializer(serializers.ModelSerializer):
  class Meta:
    model = DetalleAtencionServicioModel
    fields = '__all__'

class OrdenLaboratorioSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrdenLaboratorioModel
    fields = '__all__'

class RecordatorioSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecordatorioModel
    fields = '__all__'

class Recordatorio2Serializer(serializers.ModelSerializer):
  class Meta:
    model = RecordatorioModel
    fields = '__all__'

class DetalleOrdenAnalisisSerializer(serializers.ModelSerializer):
  class Meta:
    model = DetalleOrdenAnalisisModel
    fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ResultadoModel
    fields = '__all__'

class Resultado2Serializer(serializers.ModelSerializer):
  class Meta:
    model = RecordatorioModel
    fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = PacienteModel
    fields = '__all__'

class HistoriaClinicaSerializer(serializers.ModelSerializer):
  Cliente = ClienteSerializer()
  Paciente = PacienteSerializer()
  class Meta:
    model = HClinicaModel
    fields = ('HClinicaID','FechaApertura','observacion','Cliente','Paciente')


class cambiarpassword(serializers.Serializer):
  newpasssword = serializers.CharField(required=True)
  confirmpasssword = serializers.CharField(required=True)


class PacienteHclinica(serializers.ModelSerializer):
  Cliente = serializers.StringRelatedField
  class Meta:
    model = PacienteModel
    fields = ('Raza','Cliente','Nombre','FechaNac','Sexo','Peso','CodigoChip','Foto','observacion',)
    extra_kwargs = {
              'Estado': {
                  'read_only': True
              }
          }

class ListaProductosSerializer(serializers.Serializer):
  ProductoID = serializers.IntegerField()
  Cantidad = serializers.FloatField()
  
class RegistrarVentaSerializer(serializers.Serializer):
  Cliente = serializers.IntegerField()
  Direccion = serializers.CharField()
  Descuento = serializers.FloatField()
  Productos = ListaProductosSerializer(many=True)

class ListaDetalleatencionClinica(serializers.Serializer):
  TipoDetalleAtencion = serializers.IntegerField()
  Diagnostico = serializers.IntegerField()
  Areatrab = serializers.IntegerField()
  Trabajador = serializers.IntegerField()
  Pronostico = serializers.CharField(allow_blank=True)
  Cantidad = serializers.FloatField()
  Recordatorio = serializers.BooleanField()
  Observacion = serializers.CharField(allow_blank=True)

class ListaDetalleatencionServicio(serializers.Serializer):
  TipoDetalleAtencion = serializers.IntegerField()
  Areatrab = serializers.IntegerField()
  Servicio = serializers.IntegerField()
  Trabajador = serializers.IntegerField()
  Cantidad = serializers.FloatField()
  Recordatorio = serializers.BooleanField()
  Observacion = serializers.CharField(allow_blank=True)

class RegistrarAtencionSerializer(serializers.Serializer):
  HClinica = serializers.IntegerField()
  SiguienteAtencion = serializers.DateField(allow_null=True)
  Descuento = serializers.FloatField()
  DetallesClinicos = ListaDetalleatencionClinica(many=True,allow_null=True)
  DetallesServicios = ListaDetalleatencionServicio(many=True,allow_null=True)


class ListaOrdenLab(serializers.Serializer):
  Analisis = serializers.IntegerField()
  Observacion = serializers.CharField(allow_blank=True)

class RegistrarOrdenLabSerializer(serializers.Serializer):
  Atencion = serializers.IntegerField()
  Trabajador = serializers.IntegerField()
  Descuento = serializers.FloatField()
  DetallesLaboratorio = ListaOrdenLab(many=True,allow_null=True)