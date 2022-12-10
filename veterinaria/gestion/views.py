from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import EspecieModel
from .serializers import EspecieSerializer



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
    queryset= EspecieModel.objects.all()

    """
    def get_queryset(self):
        return self.get_serializer().meta.model.objects.filter(nombreEspecie = pk)
    """

