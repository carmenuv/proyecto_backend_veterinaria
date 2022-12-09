from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import EspecieModel, DiagnosticoModel, ServicioModel
from .serializers import EspecieSerializer, DiagnosticoSerializer, ServicioSerializer



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
      },status=status.HTTP_400_BAD_REQUEST),
      
    else:
      nuevoDiagnostico = informacion.save()
      nuevoDiagnosticoSerializada = self.serializer_class(instance = nuevoDiagnostico)
      
      return Response(data = {
        'message': 'Especie creada exitosamente',
        'content': nuevoDiagnosticoSerializada.data
      },status = status.HTTP_201_CREATED)

  def get(self, request: Request):
      Especies = EspecieModel.objects.all()
      especies_serializados = self.serializer_class(instance=Especies, many=True)
      return Response(data={
            'message': 'Las especies son:',
            'content': especies_serializados.data
      })


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
