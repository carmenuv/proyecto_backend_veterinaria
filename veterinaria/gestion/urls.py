from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import *

urlpatterns = [
    path('iniciar-sesion/', TokenObtainPairView.as_view()),
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
    path('registro-producto/', ProductoApiView.as_view()),
    path('actualizar-producto/<str:pk>', ProductoToggleApiView.as_view()),

    path('registrar-cliente/', ClienteApiView.as_view()),
    path('actualizar-cliente/<str:pk>', ClienteToggleApiView.as_view()),
    path('flltrar-cliente/', ClientWithFilters.as_view()),

    path('registrar-trabajador/', TrabajadorApiView.as_view()),
    path('actualizar-trabajador/<str:pk>', TrabajadorToggleApiView.as_view()),
    path('flltrar-trabajador/', WorkerWithFilters.as_view()),

    path('registro-almacen/', AlmacenApiView.as_view()),
    path('actualizar-almacen/<str:pk>', AlmacenToggleApiView.as_view()),
    path('registro-cita/', CitaApiView.as_view()),
    path('actualizar-cita/<str:pk>', CitaToggleApiView.as_view()),

    path('registrar-area-servicio/',AreaServicioApiView .as_view()),
    path('actualizar-area-servicio/<str:pk>', AreaServicioToggleApiView.as_view()),    
    path('registrar-servicio-trabajador/', ServicioTrabajadorApiView.as_view()),
    path('actualizar-servicio-trabajador/<str:pk>', ServicioToggleApiView.as_view()),

    path('registro-venta/', VentaApiView.as_view()),
    path('actualizar-venta/<str:pk>', VentaToggleApiView.as_view()),
    path('registro-detalleventa/', DetalleVentaApiView.as_view()),
    path('actualizar-detalleventa/<str:pk>', DetalleVentaToggleApiView.as_view()),

    path('registro-atencion/', AtencionApiView.as_view()),
    path('actualizar-atencion/<str:pk>', AtencionToggleApiView.as_view()),
    path('registro-detalleatencion/', DetalleAtencionApiView.as_view()),
    path('actualizar-detalleatencion/<str:pk>', DetalleAtencionToggleApiView.as_view()),

    path('registro-ordenlaboratorio/', OrdenLaboratorioApiView.as_view()),
    path('actualizar-ordenlaboratorio/<str:pk>', OrdenLaboratorioToggleApiView.as_view()),
    path('registro-orecordatorioo/', RecordatorioApiView.as_view()),
    path('actualizar-recordatorio/<str:pk>', RecordatorioToggleApiView.as_view()),

    path('registro-detalleordenanalisis/', DetalleOrdenAnalisisApiView.as_view()),
    path('actualizar-detalleordenanalisis/<str:pk>', DetalleOrdenAnalisisToggleApiView.as_view()),
    path('registro-resultado/', ResultadoApiView.as_view()),
    path('actualizar-resultado/<str:pk>', ResultadoToggleApiView.as_view()),

    path('registrar-clienteUsu/', ClienteRegistro.as_view()),

]