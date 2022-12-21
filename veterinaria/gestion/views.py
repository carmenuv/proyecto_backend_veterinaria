from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import EspecieModel,TipoDetalleAtencionModel,RazaModel, DiagnosticoModel, ServicioModel, AreaModel, TipoDocumentoModel, AnalisisModel, TipoTrabajadorModel, TipoProductoModel
from .serializers import EspecieSerializer,TipoDetalleAtencionSerializer,RazaSerializer, DiagnosticoSerializer, ServicioSerializer, AreaSerializer, TipoDocumentoSerializer, AnalisisSerializer, TipoTrabajadorSerializer, TipoProductoSerializer
from .models import *
from .serializers import *

#Especie==========================================================================================
class EspecieApiView(ListCreateAPIView):
  serializer_class = EspecieSerializer
  queryset = EspecieModel.objects.all()

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear la especie',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevaEspecie = informacion.save()
      nuevaEspecieSerializada = self.serializer_class(instance = nuevaEspecie)
      
      return Response(data = {
        'message': 'Especie creada exitosamente',
        'content': nuevaEspecieSerializada.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Especies = EspecieModel.objects.all()
      especies_serializados = self.serializer_class(instance=Especies, many=True)
      return Response(data={
            'message': 'Las especies son:',
            'content': especies_serializados.data
      })

  def get_queryset(self, request: Request):
      return EspecieModel.objects.all()


class EspecieToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = EspecieSerializer
  
  def get(self, request: Request,pk):
    Especies = EspecieModel.objects.filter(EspecieID = pk).first()
    especies_serializados = self.serializer_class(instance=Especies)
    return Response(especies_serializados.data)

  def put(self, request:Request, pk: str):

      especie=EspecieModel.objects.filter(EspecieID = pk).first()
      serializer=EspecieSerializer(especie,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      especie=EspecieModel.objects.filter(EspecieID = pk).first()
      especie.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

#TipoDetalleAtencion==========================================================================================
class TipoDetalleAtencionApiView(ListCreateAPIView):
  serializer_class = TipoDetalleAtencionSerializer
  queryset = TipoDetalleAtencionModel.objects.all()

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el tipo de detalle de atencion',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoTipoDetalleAtencion = informacion.save()
      nuevoTipoDetalleAtencion_Serializado = self.serializer_class(instance = nuevoTipoDetalleAtencion)
      
      return Response(data = {
        'message': 'Tipo De Detalle Creado exitosamente',
        'content': nuevoTipoDetalleAtencion_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      TiposDetalleAtencion = TipoDetalleAtencionModel.objects.all()
      nuevoTipoDetalleAtencion_Serializado = self.serializer_class(instance=TiposDetalleAtencion, many=True)
      return Response(data={
            'message': 'Los Detalles de Atencion son:',
            'content': nuevoTipoDetalleAtencion_Serializado.data
      })

class TipoDetalleAtencionToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = TipoDetalleAtencionSerializer
  
  def get(self, request: Request,pk):
    TipoDetalleAtencion = TipoDetalleAtencionModel.objects.filter(TipoDetalleAtencionID = pk).first()
    nuevoTipoDetalleAtencion_Serializado = self.serializer_class(instance=TipoDetalleAtencion)
    return Response(nuevoTipoDetalleAtencion_Serializado.data)

  def put(self, request:Request, pk: str):

      TipoDetalleAtencion=TipoDetalleAtencionModel.objects.filter(TipoDetalleAtencionID = pk).first()
      serializer=TipoDetalleAtencionSerializer(TipoDetalleAtencion,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      TipoDetalleAtencion=TipoDetalleAtencionModel.objects.filter(TipoDetalleAtencionID = pk).first()
      TipoDetalleAtencion.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

#Raza==========================================================================================
class RazaApiView(ListCreateAPIView):
  serializer_class = RazaSerializer
  queryset = RazaModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear la raza',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevaRaza = informacion.save()
      nuevaRaza_Serializada = self.serializer_class(instance = nuevaRaza)
      
      return Response(data = {
        'message': 'Nueva Raza Creada exitosamente',
        'content': nuevaRaza_Serializada.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Raza = RazaModel.objects.all()
      Raza_Serializada = self.serializer_class(instance=Raza, many=True)
      return Response(data={
            'message': 'Las razas son:',
            'content': Raza_Serializada.data
      })

class RazaToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = RazaSerializer
  
  def get(self, request: Request,pk):
    Raza = RazaModel.objects.filter(RazaID = pk).first()
    Raza_Serializado = self.serializer_class(instance=Raza)
    return Response(Raza_Serializado.data)

  def put(self, request:Request, pk: str):

      Raza=RazaModel.objects.filter(RazaID = pk).first()
      serializer=RazaSerializer(Raza,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      Raza=RazaModel.objects.filter(RazaID = pk).first()
      Raza.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

#Diagnostico==========================================================================================
class DiagnosticoApiView(ListCreateAPIView):
  serializer_class = DiagnosticoSerializer
  queryset = DiagnosticoModel.objects.all()

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el diagnóstico',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST),
      
    else:
      nuevoDiagnostico = informacion.save()
      nuevoDiagnosticoSerializado = self.serializer_class(instance = nuevoDiagnostico)
      
      return Response(data = {
        'message': 'Especie creada exitosamente',
        'content': nuevoDiagnosticoSerializado.data
      },status = status.HTTP_201_CREATED)

  def get(self, request: Request):
      Diagnosticos = DiagnosticoModel.objects.all()
      diagnosticos_serializados = self.serializer_class(instance=Diagnosticos, many=True)
      return Response(data={
            'message': 'Los diagnosticos son:',
            'content': diagnosticos_serializados.data
      })

class DiagnosticoToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = DiagnosticoSerializer
  
  def get(self, request: Request,pk):
    Diagnosticos = DiagnosticoModel.objects.filter(DiagnosticoID = pk).first()
    diagnosticos_serializados = self.serializer_class(instance=Diagnosticos)
    return Response(diagnosticos_serializados.data)

  def put(self, request:Request, pk: str):
      diagnostico=DiagnosticoModel.objects.filter(DiagnosticoID = pk).first()
      serializer=DiagnosticoSerializer(diagnostico,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      diagnostico=EspecieModel.objects.filter(DiagnosticoID = pk).first()
      diagnostico.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

#Servicio==========================================================================================
class ServicioApiView(ListCreateAPIView):
  serializer_class = ServicioSerializer
  queryset = ServicioModel.objects.all()

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el servicio',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST),
      
    else:
      nuevoServicio = informacion.save()
      nuevoServicioSerializado = self.serializer_class(instance = nuevoServicio)
      
      return Response(data = {
        'message': 'Servicio creado exitosamente',
        'content': nuevoServicioSerializado.data
      },status = status.HTTP_201_CREATED)

  def get(self, request: Request):
      Servicios = ServicioModel.objects.all()
      Servicios_serializados = self.serializer_class(instance=Servicios, many=True)
      return Response(data={
            'message': 'Los servicios son:',
            'content': Servicios_serializados.data
      })

class ServicioToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = ServicioSerializer
  
  def get(self, request: Request,pk):
    Servicios = ServicioModel.objects.filter(ServicioID = pk).first()
    servicios_serializados = self.serializer_class(instance=Servicios)
    return Response(servicios_serializados.data)

  def put(self, request:Request, pk: str):
      servicio=ServicioModel.objects.filter(ServicioID = pk).first()
      serializer=ServicioSerializer(servicio,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      servicio=ServicioModel.objects.filter(ServicioID = pk).first()
      servicio.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
        
#Area==========================================================================================
class AreaApiView(ListCreateAPIView):
  serializer_class = AreaSerializer
  queryset = AreaModel.objects.all()

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el area',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevaArea = informacion.save()
      nuevaAreaSerializada = self.serializer_class(instance = nuevaArea)
      
      return Response(data = {
        'message': 'Area creada exitosamente',
        'content': nuevaAreaSerializada.data
      },status = status.HTTP_201_CREATED)

  def get(self, request: Request):
        
        Areas = AreaModel.objects.all()
        # many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
        areas_serializadas = self.serializer_class(instance=Areas, many=True)

        return Response(data={
            'message': 'Las areas son:',
            'content': areas_serializadas.data
        }) 

class AreaToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = AreaSerializer
  
  def get(self, request: Request,pk):
    Areas = AreaModel.objects.filter(AreaID = pk).first()
    areas_serializadas = self.serializer_class(instance=Areas)
    return Response(areas_serializadas.data)

  def put(self, request:Request, pk: str):

      area=AreaModel.objects.filter(AreaID = pk).first()
      serializer=AreaSerializer(area,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      area=AreaModel.objects.filter(AreaID = pk).first()
      area.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

#TipoDocumento==========================================================================================
class TipoDocumentoApiView(ListCreateAPIView):
  serializer_class = TipoDocumentoSerializer
  queryset = TipoDocumentoModel.objects.all()

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el documento',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoDocumento = informacion.save()
      nuevaDocumentoserilizado = self.serializer_class(instance = nuevoDocumento)
      
      return Response(data = {
        'message': 'Documento creado exitosamente',
        'content': nuevaDocumentoserilizado.data
      },status = status.HTTP_201_CREATED)

  def get(self, request: Request):
        
        Documento = TipoDocumentoModel.objects.all()
        # many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
        documentos_serializados = self.serializer_class(instance=Documento, many=True)

        return Response(data={
            'message': 'Los documentos son:',
            'content': documentos_serializados.data
        }) 


class DocumentoToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = TipoDocumentoSerializer
  
  def get(self, request: Request,pk):
    Documentos = TipoDocumentoModel.objects.filter(TipoDocumentoID = pk).first()
    documentos_serializados = self.serializer_class(instance=Documentos)
    return Response(documentos_serializados.data)

  def put(self, request:Request, pk: str):

      documento=TipoDocumentoModel.objects.filter(TipoDocumentoID = pk).first()
      serializer=TipoDocumentoSerializer(documento,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      documento=TipoDocumentoModel.objects.filter(TipoDocumentoID= pk).first()
      documento.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


#Analisis==========================================================================================
class AnalisisApiView(ListCreateAPIView):
  serializer_class = AnalisisSerializer
  queryset = AnalisisModel.objects.all()

  def get(self,request:Request):
      
    Analisis = AnalisisModel.objects.all()
    # many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
    analisis_serializados = self.serializer_class(instance=Analisis, many=True)

    return Response(data={
        'message': 'Los análisis son:',
        'content': analisis_serializados.data
    })

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el análisis',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoAnalisis = informacion.save()
      nuevoAnalisisSerializado = self.serializer_class(instance = nuevoAnalisis)
      
      return Response(data = {
        'message': 'Análisis creado exitosamente',
        'content': nuevoAnalisisSerializado.data
      },status = status.HTTP_201_CREATED)

class AnalisisToggleApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = AnalisisSerializer
  
  def get(self, request: Request,pk):
    Analisis = AnalisisModel.objects.filter(AnalisisID = pk).first()
    analisis_serializados = self.serializer_class(instance=Analisis)
    return Response(analisis_serializados.data)

  def put(self, request:Request, pk: str):

      analisis=AnalisisModel.objects.filter(AnalisisID = pk).first()
      serializer=AnalisisSerializer(analisis,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      analisis=AnalisisModel.objects.filter(AnalisisID = pk).first()
      analisis.delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 

#TipoTrabajador==========================================================================================
class TipoTrabajadorApiView(ListCreateAPIView):
  serializer_class = TipoTrabajadorSerializer
  queryset = TipoTrabajadorModel.objects.all()

  def get(self,request:Request):
      
    tipoTrabajador = TipoTrabajadorModel.objects.all()
    # many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
    tipoTrabajador_serializados = self.serializer_class(instance=tipoTrabajador, many=True)

    return Response(data={
        'message': 'Los tipos de trabajador son:',
        'content': tipoTrabajador_serializados.data
    })

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el tipo de trabajador',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoTipoTrabajador = informacion.save()
      nuevoTipoTrabajadorSerializado = self.serializer_class(instance = nuevoTipoTrabajador)
      
      return Response(data = {
        'message': 'Tipo trabajdor creado exitosamente',
        'content': nuevoTipoTrabajadorSerializado.data
      },status = status.HTTP_201_CREATED)

class TipoTrabajadorToggleApiView(RetrieveUpdateDestroyAPIView):

  serializer_class = TipoTrabajadorSerializer

  
  def get(self, request: Request,pk):
    TipoTrabajadores = TipoTrabajadorModel.objects.filter(TipoTrabajadorID = pk).first()
    tipoTrabajadores_serializados = self.serializer_class(instance=TipoTrabajadores)
    return Response(tipoTrabajadores_serializados.data)

  def put(self, request:Request, pk: str):

      tipoTrabajador=TipoTrabajadorModel.objects.filter(TipoTrabajadorID = pk).first()
      serializer=TipoTrabajadorSerializer(tipoTrabajador,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      tipoTrabajador=TipoTrabajadorModel.objects.filter(TipoTrabajadorID = pk).first()
      tipoTrabajador.delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 



#ALMACEN==========================================================================================
class AlmacenApiView(ListCreateAPIView):
  serializer_class = AlmacenSerializer
  queryset = AlmacenModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el almacen',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoAlmacen = informacion.save()
      nuevoAlmacen_Serializado = self.serializer_class(instance = nuevoAlmacen)
      
      return Response(data = {
        'message': 'Nuevo almacen creado exitosamente',
        'content': nuevoAlmacen_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Almacen = AlmacenModel.objects.all()
      Almacen_Serializado = self.serializer_class(instance=Almacen, many=True)
      return Response(data={
            'message': 'Los almacenes son:',
            'content': Almacen_Serializado.data
      })

class AlmacenToggleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = Almacen2Serializer
    
    def get(self, request: Request,pk):
      Almacen = AlmacenModel.objects.filter(AlmacenID = pk).first()
      Almacen_Serializado = self.serializer_class(instance=Almacen)
      return Response(Almacen_Serializado.data)

    def patch(self, request:Request, pk: str):
        Almacen=AlmacenModel.objects.filter(AlmacenID = pk).first()
        if Almacen:
          Almacen_Serializado = self.serializer_class(instance=Almacen)
          return Response(Almacen_Serializado.data,status=status.HTTP_200_OK)
        return Response(Almacen_Serializado.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request:Request, pk: str):
        Almacen=AlmacenModel.objects.filter(AlmacenID = pk).first()
        serializer=self.serializer_class(Almacen,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, pk: str):
        Almacen=AlmacenModel.objects.filter(AlmacenID = pk).first()
        Almacen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#CITAS
#Prodcuto==========================================================================================
class CitaApiView(ListCreateAPIView):
  serializer_class = CitaSerializer
  queryset = CitaModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear la cita',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevaCita = informacion.save()
      nuevaCita_Serializado = self.serializer_class(instance = nuevaCita)
      
      return Response(data = {
        'message': 'Nuevo producto creado exitosamente',
        'content': nuevaCita_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Cita = CitaModel.objects.all()
      Cita_Serializado = self.serializer_class(instance=Cita, many=True)
      return Response(data={
            'message': 'Las citas son:',
            'content': Cita_Serializado.data
      })

class CitaToggleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = Cita2Serializer
    
    def get(self, request: Request,pk):
      Cita = CitaModel.objects.filter(CitasID = pk).first()
      Cita_Serializado = self.serializer_class(instance=Cita)
      return Response(Cita_Serializado.data)

    def patch(self, request:Request, pk: str):
        Cita=CitaModel.objects.filter(CitasID = pk).first()
        if Cita:
          Cita_Serializado = self.serializer_class(instance=Cita)
          return Response(Cita_Serializado.data,status=status.HTTP_200_OK)
        return Response(Cita_Serializado.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request:Request, pk: str):
        Cita=CitaModel.objects.filter(ProductoID = pk).first()
        serializer=self.serializer_class(Cita,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, pk: str):
        Cita=CitaModel.objects.filter(CitasID = pk).first()
        Cita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#tipoUsuario
class TipoUsuarioApiView(ListCreateAPIView):
  serializer_class = TipoUsuarioSerializer
  queryset = CitaModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el tipo de usuario',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoTipoUsuario = informacion.save()
      nuevoTipoUsuario_Serializado = self.serializer_class(instance = nuevoTipoUsuario)
      
      return Response(data = {
        'message': 'Nuevo tipo de usuario creado exitosamente',
        'content': nuevoTipoUsuario_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      TipoUsuario = CitaModel.objects.all()
      TipoUsuario_Serializado = self.serializer_class(instance=TipoUsuario, many=True)
      return Response(data={
            'message': 'Las citas son:',
            'content': TipoUsuario_Serializado.data
      })

class TipoUsuarioToggleApiView(RetrieveUpdateDestroyAPIView):

  serializer_class = TipoUsuarioSerializer

  
  def get(self, request: Request,pk):
    TipoUsuario = TipoUsuarioModel.objects.filter(TipoUsuarioID = pk).first()
    tipoUsuarios_serializados = self.serializer_class(instance=TipoUsuario)
    return Response(tipoUsuarios_serializados.data)

  def put(self, request:Request, pk: str):

      tipoUsuario=TipoUsuarioModel.objects.filter(TipoUsuarioID = pk).first()
      serializer=TipoUsuarioSerializer(tipoUsuario,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      tipoUsuario=TipoTrabajadorModel.objects.filter(TipoUsuarioID = pk).first()
      tipoUsuario.delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 


#Recordatorio
class RecordatorioApiView(ListCreateAPIView):
  serializer_class = RecordatorioSerializer
  queryset = RecordatorioModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el recordatorio',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoRecordatorio = informacion.save()
      nuevoRecordatorio_Serializado = self.serializer_class(instance = nuevoRecordatorio)
      
      return Response(data = {
        'message': 'Nuevo recordatorio creado exitosamente',
        'content': nuevoRecordatorio_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Recordatorio = RecordatorioModel.objects.all()
      Recordatorio_Serializado = self.serializer_class(instance=Recordatorio, many=True)
      return Response(data={
            'message': 'Las recordatorios son:',
            'content': Recordatorio_Serializado.data
      })



class RecordatorioToggleApiView(RetrieveUpdateDestroyAPIView):

  serializer_class = RecordatorioSerializer
  
  def get(self, request: Request,pk):
    Recordatorio = RecordatorioModel.objects.filter(RecordatorioID = pk).first()
    recordatorio_serializados = self.serializer_class(instance=Recordatorio)
    return Response(recordatorio_serializados.data)

  def put(self, request:Request, pk: str):

      recordatorio=RecordatorioModel.objects.filter(RecordatorioID = pk).first()
      serializer=RecordatorioSerializer(recordatorio,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      recordatorio=RecordatorioModel.objects.filter(RecordatorioID = pk).first()
      recordatorio.delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 


#RESULTADO
class ResultadoApiView(ListCreateAPIView):
  serializer_class = ResultadoSerializer
  queryset = ResultadoModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el resultado correspondiente',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoResultado = informacion.save()
      nuevoResultado_Serializado = self.serializer_class(instance = nuevoResultado)
      
      return Response(data = {
        'message': 'Nuevo resultado creado exitosamente',
        'content': nuevoResultado_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Resultado = ResultadoModel.objects.all()
      Resultado_Serializado = self.serializer_class(instance=Resultado, many=True)
      return Response(data={
            'message': 'Las recordatorios son:',
            'content': Resultado_Serializado.data
      })



class ResultadoToggleApiView(RetrieveUpdateDestroyAPIView):

  serializer_class = ResultadoSerializer
  
  def get(self, request: Request,pk):
    resultado = ResultadoModel.objects.filter(ResultadoID = pk).first()
    resultado_serializados = self.serializer_class(instance=resultado)
    return Response(resultado_serializados.data)

  def put(self, request:Request, pk: str):

      resultado=ResultadoModel.objects.filter(ResultadoID = pk).first()
      serializer=ResultadoSerializer(resultado,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request:Request, pk: str):
      resultado=ResultadoModel.objects.filter(ResultadoID = pk).first()
      resultado.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
