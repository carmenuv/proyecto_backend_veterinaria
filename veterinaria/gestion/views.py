from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import EspecieModel
from .serializers import EspecieSerializer

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
      nuevaEspecie = informacion.save()
      nuevaEspecieSerializada = self.serializer_class(instance = nuevaEspecie)
      
      return Response(data = {
        'message': 'Especie creada exitosamente',
        'content': nuevaEspecieSerializada.data
      },status = status.HTTP_201_CREATED)

  def get(self,request:Request):
    especies = EspecieModel.objects.all()
    especies_serializados = self.serializer_class(instance=especies,many=True)

    return Response(data={
      'message':'Las especies es:',
      'content': especies_serializados.data
    })

class EspecieToggleApiView(UpdateAPIView):
  
  serializer_class = EspecieModel
  queryset = EspecieModel.objects.all()

  def put(self,request:Request,EspecieId:str):
    especieEncontrada = EspecieModel.objects.filter(EspecieId = EspecieId).first()

    especieEncontrada.save()

    if especieEncontrada is None:
      return Response(data={
        'message': 'Especie no encontrada'
      },status = status.HTTP_404_NOT_FOUND)

    return Response(data={
      'message': 'Especie actualizada exitosamente',
       
    },status = status.HTTP_201_CREATED)
  

