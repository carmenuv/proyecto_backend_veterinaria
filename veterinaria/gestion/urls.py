from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import *

urlpatterns = [
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('registro-especie/', EspecieApiView.as_view()),
    path('actualizar-especie/<str:pk>', EspecieToggleApiView.as_view()),    
    path('registro-tipodetalleatencion/', TipoDetalleAtencionApiView.as_view()),
    path('actualizar-tipodetalleatencion/<str:pk>', TipoDetalleAtencionToggleApiView.as_view()),
    path('registro-raza/', RazaApiView.as_view()),
    path('actualizar-raza/<str:pk>', RazaToggleApiView.as_view()),

    path('registro-diagnostico/', DiagnosticoApiView.as_view()),
    path('actualizar-diagnostico/<str:pk>', DiagnosticoToggleApiView.as_view()),
    path('registro-servicio/', ServicioApiView.as_view()),
    path('actualizar-servicio/<str:pk>', ServicioToggleApiView.as_view()),

    path('registro-area/', AreaApiView.as_view()),
    path('actualizar-area/<str:pk>', AreaToggleApiView.as_view()),
    path('registro-documento/', TipoDocumentoApiView.as_view()),
    path('actualizar-documento/<str:pk>', DocumentoToggleApiView.as_view()),

    path('registro-analisis/', AnalisisApiView.as_view()),
    path('actualizar-analisis/<str:pk>', AnalisisToggleApiView.as_view()),
    path('registro-tipoTrabajador/', TipoTrabajadorApiView.as_view()),
    path('actualizar-tipoTrabajador/<str:pk>', TipoTrabajadorToggleApiView.as_view()),

    path('registro-tipoproducto/', TipoProductoApiView.as_view()),
    path('actualizar-tipoproducto/<str:pk>', TipoProductoToggleApiView.as_view()),

    path('registrar-cliente/', ClienteApiView.as_view()),
    path('actualizar-cliente/<str:pk>', ClienteToggleApiView.as_view()),
    path('flltrar-cliente/', ClientWithFilters.as_view()),

    path('registrar-trabajador/', TrabajadorApiView.as_view()),
    path('actualizar-trabajador/<str:pk>', TrabajadorToggleApiView.as_view()),
    path('flltrar-trabajador/', WorkerWithFilters.as_view()),
]