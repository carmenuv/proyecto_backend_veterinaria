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


class EspecieToggleApiView(RetrieveUpdateDestroyAPIView):
    
        
    serializer_class = EspecieSerializer
    queryset= EspecieModel.objects.all()


    """


    serializer_class = EspecieSerializer
    queryset= EspecieModel.objects.all()

    def put(self, request:Request, pk: str):
        # primero busco si existe el plato
        # SELECT * FROM platos WHERE id = ... LIMIT 1;
        print(pk)
        especieEncontrada = EspecieModel.objects.filter(nombreEspecie = pk).first()

        if especieEncontrada is None:
            return Response(data={
                'message': 'plato no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # actualizare el estado de la disponibilidad
        # la nueva disponibilidad sera la anterior al reves
        especieEncontrada.disponibilidad = not especieEncontrada.disponibilidad

        especieEncontrada.save()

        return Response(data={
            'message': 'plato actualizado exitosamente',
            'content': self.serializer_class(instance=especieEncontrada).data
        }, status=status.HTTP_201_CREATED)

        """