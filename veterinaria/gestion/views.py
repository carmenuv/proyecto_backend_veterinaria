from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import EspecieModel,TipoDetalleAtencionModel,RazaModel
from .serializers import EspecieSerializer,TipoDetalleAtencionSerializer,RazaSerializer


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
