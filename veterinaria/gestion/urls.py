from django.urls import path

from .views import EspecieApiView,EspecieToggleApiView,TipoDetalleAtencionApiView,TipoDetalleAtencionToggleApiView,RazaApiView, RazaToggleApiView, DiagnosticoApiView, DiagnosticoToggleApiView, ServicioApiView, ServicioToggleApiView, AreaApiView,AreaToggleApiView,TipoDocumentoApiView,DocumentoToggleApiView


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
]