from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import EspecieModel
from .models import AnalisisModel
from .models import TipoTrabajadorModel

from .serializers import EspecieSerializer
from .serializers import AnalisisSerializer
from .serializers import TipoTrabajadorSerializer


#Especie==========================================================================================
class EspecieApiView(ListCreateAPIView):
  serializer_class = EspecieSerializer
  queryset = EspecieModel.objects.all()

  def get(self,request:Request):
      
    Especies = EspecieModel.objects.all()
    # many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
    especies_serializados = self.serializer_class(instance=Especies, many=True)

    return Response(data={
        'message': 'Las especies son:',
        'content': especies_serializados.data
    })

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


#Analisis==========================================================================================
class AnalisisApiView(ListCreateAPIView):
  serializer_class = AnalisisSerializer
  queryset = AnalisisModel.objects.all()

  def get(self,request:Request):
      
    Analisis = AnalisisModel.objects.all()
    # many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
    analisis_serializados = self.serializer_class(instance=Analisis, many=True)

    return Response(data={
        'message': 'Las analisis son:',
        'content': analisis_serializados.data
    })

  def post(self, request:Request):
    informacion = self.serializer_class(data=request.data)
    es_valida = informacion.is_valid()

    if not es_valida:
      return Response(data={
        'message': 'Error al crear el analisis',
        'content': informacion.errors
      },status=status.HTTP_400_BAD_REQUEST)
    else:
      nuevoAnalisis = informacion.save()
      nuevoAnalisisSerializado = self.serializer_class(instance = nuevoAnalisis)
      
      return Response(data = {
        'message': 'Analisis creado exitosamente',
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
        'message': 'Las tipos de trabajador son:',
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
      tipoTrabajdores_serializados = self.serializer_class(instance=TipoTrabajadores)
      return Response(tipoTrabajdores_serializados.data)

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