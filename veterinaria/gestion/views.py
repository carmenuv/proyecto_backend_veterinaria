from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, filters
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


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
    serializer_class = Raza2Serializer
    
    def get(self, request: Request,pk):
      Raza = RazaModel.objects.filter(RazaID = pk).first()
      Raza_Serializado = self.serializer_class(instance=Raza)
      return Response(Raza_Serializado.data)

    def patch(self, request:Request, pk: str):
        Raza=RazaModel.objects.filter(RazaID = pk).first()
        if Raza:
          Raza_Serializado = self.serializer_class(instance=Raza)
          return Response(Raza_Serializado.data,status=status.HTTP_200_OK)
        return Response(Raza_Serializado.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request:Request, pk: str):
        Raza=RazaModel.objects.filter(RazaID = pk).first()
        serializer=self.serializer_class(Raza,data=request.data)

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

#TipoProducto========================================================================================== 
class TipoProductoApiView(ListCreateAPIView):
  serializer_class = TipoProductoSerializer
  queryset = TipoProductoModel.objects.all()

  def get(self,request:Request):
      
    tipoProducto = TipoProductoModel.objects.all()
    # many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
    tipoProducto_serializados = self.serializer_class(instance=tipoProducto, many=True)

    return Response(data={
        'message': 'Los tipos de producto son:',
        'content': tipoProducto_serializados.data
    })

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el tipo de producto',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoTipoProducto = informacion.save()
      nuevoTipoProductoSerializado = self.serializer_class(instance = nuevoTipoProducto)
      
      return Response(data = {
        'message': 'Tipo producto creado exitosamente',
        'content': nuevoTipoProductoSerializado.data
      },status = status.HTTP_201_CREATED)

class TipoProductoToggleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TipoProductoSerializer
    
    def get(self, request: Request,pk):
      TipoProductos = TipoProductoModel.objects.filter(TipoProductoID = pk).first()
      tipoProductos_serializados = self.serializer_class(instance=TipoProductos)
      return Response(tipoProductos_serializados.data)

    def put(self, request:Request, pk: str):

        tipoProducto=TipoProductoModel.objects.filter(TipoProductoID = pk).first()
        serializer=TipoProductoSerializer(tipoProducto,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, pk: str):
        tipoProducto=TipoProductoModel.objects.filter(TipoProductoID = pk).first()
        tipoProducto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Prodcuto==========================================================================================
class ProductoApiView(ListCreateAPIView):
  serializer_class = ProductoSerializer
  queryset = ProductoModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el producto',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoProducto = informacion.save()
      nuevoProducto_Serializado = self.serializer_class(instance = nuevoProducto)
      
      return Response(data = {
        'message': 'Nuevo producto creado exitosamente',
        'content': nuevoProducto_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Producto = ProductoModel.objects.all()
      Producto_Serializado = self.serializer_class(instance=Producto, many=True)
      return Response(data={
            'message': 'Los productos son:',
            'content': Producto_Serializado.data
      })

class ProductoToggleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = Producto2Serializer
    
    def get(self, request: Request,pk):
      Producto = ProductoModel.objects.filter(ProductoID = pk).first()
      Producto_Serializado = self.serializer_class(instance=Producto)
      return Response(Producto_Serializado.data)

    def patch(self, request:Request, pk: str):
        Producto=ProductoModel.objects.filter(ProductoID = pk).first()
        if Producto:
          Producto_Serializado = self.serializer_class(instance=Producto)
          return Response(Producto_Serializado.data,status=status.HTTP_200_OK)
        return Response(Producto_Serializado.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request:Request, pk: str):
        Producto=ProductoModel.objects.filter(ProductoID = pk).first()
        serializer=self.serializer_class(Producto,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, pk: str):
        Producto=ProductoModel.objects.filter(ProductoID = pk).first()
        Producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Cliente==========================================================================================
class ClienteApiView(ListCreateAPIView):
  serializer_class = ClienteSerializer
  queryset = ClienteModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el cliente',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoCliente = informacion.save()
      nuevoCliente_Serializado = self.serializer_class(instance = nuevoCliente)
      
      return Response(data = {
        'message': 'Nueva cliente Creado exitosamente',
        'content': nuevoCliente_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Cliente = ClienteModel.objects.filter(Estado = 'HABILITADO')
      Clientes_Serializados = self.serializer_class(instance=Cliente, many=True)
      return Response(data={
            'message': 'Los clientes son:',
            'content': Clientes_Serializados.data
      })

class ClienteToggleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = Cliente2Serializer
    
    def get(self, request: Request,pk):
      Cliente = ClienteModel.objects.filter(ClienteID = pk).first()
      Cliente_Serializado = self.serializer_class(instance=Cliente)
      return Response(Cliente_Serializado.data)

    def patch(self, request:Request, pk: str):
        Cliente = ClienteModel.objects.filter(ClienteID = pk).first()
        if Cliente:
          Cliente_Serializado = self.serializer_class(instance=Cliente)
          return Response(Cliente_Serializado.data,status=status.HTTP_200_OK)
        return Response(Cliente_Serializado.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request:Request, pk: str):
        Cliente = ClienteModel.objects.filter(ClienteID = pk).first()
        serializer=self.serializer_class(Cliente,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, pk: str):
        Cliente = ClienteModel.objects.filter(ClienteID = pk).first()
        if Cliente is None:
              return Response(data={
                  'message': 'Cliente no encontrado'
              }, status=status.HTTP_404_NOT_FOUND)

        Cliente.Estado = 'DESHABILITADO'
        Cliente.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClientWithFilters(ListAPIView):
      queryset = ClienteModel.objects.all().select_related('TipoDocumento')
      serializer_class = ClienteSerializer
      filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
      filterset_fields = {
        'Documento': ['contains'],
        'Nombre': ['contains'],
        'ApePaterno': ['contains'],
        'ApeMaterno': ['contains'],
        'NroContacto': ['contains'],
        'Direccion': ['contains'],
        'Correo': ['contains'],
        'observacion': ['contains']
      }
      search_fields = ['Documento', 'Nombre','ApePaterno','ApeMaterno','NroContacto','Direccion','Correo','observacion']
      ordering_fields = ['Documento', 'Nombre','ApePaterno','ApeMaterno','NroContacto','Direccion','Correo','observacion']
      ordering = ['ApePaterno']

#Trabajador==========================================================================================

class TrabajadorApiView(ListCreateAPIView):
  serializer_class = TrabajadorSerializer

  queryset = TrabajadorModel.objects.all()

  def create(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el Trabajador',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoTrabajador = informacion.save()
      nuevoTrabajador_Serializado = self.serializer_class(instance = nuevoTrabajador)
      
      return Response(data = {
        'message': 'Nueva Trabajador Creado exitosamente',
        'content': nuevoTrabajador_Serializado.data
      },status = status.HTTP_201_CREATED)


  def get(self, request: Request):
      Trabajador = TrabajadorModel.objects.filter(Estado = 'HABILITADO')
      Trabajadores_Serializados = self.serializer_class(instance=Trabajador, many=True)
      return Response(data={
            'message': 'Los trabajadores son:',
            'content': Trabajadores_Serializados.data
      })

class TrabajadorToggleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = Trabajador2Serializer
    
    def get(self, request: Request,pk):
      Trabajador = TrabajadorModel.objects.filter(TrabajadorID = pk).first()
      Trabajador_Serializado = self.serializer_class(instance=Trabajador)
      return Response(Trabajador_Serializado.data)

    def patch(self, request:Request, pk: str):
        Trabajador = TrabajadorModel.objects.filter(TrabajadorID = pk).first()
        if Trabajador:
          Trabajador_Serializado = self.serializer_class(instance=Trabajador)
          return Response(Trabajador_Serializado.data,status=status.HTTP_200_OK)
        return Response(Trabajador_Serializado.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request:Request, pk: str):
        Trabajador = TrabajadorModel.objects.filter(TrabajadorID = pk).first()
        serializer=self.serializer_class(Trabajador,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, pk: str):
        Trabajador = TrabajadorModel.objects.filter(TrabajadorID = pk).first()
        if Trabajador is None:
              return Response(data={
                  'message': 'Trabajador no encontrado'
              }, status=status.HTTP_404_NOT_FOUND)

        Trabajador.Estado = 'DESHABILITADO'
        Trabajador.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WorkerWithFilters(ListAPIView):
      queryset = TrabajadorModel.objects.all().select_related('TipoDocumento').select_related('TipoTrabajador')
      serializer_class = TrabajadorSerializer
      filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
      filterset_fields = {
        'Documento': ['contains'],
        'Nombre': ['contains'],
        'ApePaterno': ['contains'],
        'ApeMaterno': ['contains'],
        'NroContacto': ['contains'],
        'Direccion': ['contains'],
        'Correo': ['contains'],
        'observacion': ['contains']
      }
      search_fields = ['Documento', 'Nombre','ApePaterno','ApeMaterno','NroContacto','Direccion','Correo','observacion']
      ordering_fields = ['Documento', 'Nombre','ApePaterno','ApeMaterno','NroContacto','Direccion','Correo','observacion']
      ordering = ['ApePaterno']

#Almacen==========================================================================================
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


#Citas==========================================================================================
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
