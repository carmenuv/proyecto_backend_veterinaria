from django.urls import path
from .views import EspecieApiView,EspecieToggleApiView,TipoDetalleAtencionApiView,TipoDetalleAtencionToggleApiView,RazaApiView,RazaToggleApiView

urlpatterns = [
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('registro-especie/', EspecieApiView.as_view()),
    path('actualizar-especie/<str:pk>', EspecieToggleApiView.as_view()),
    path('registro-tipodetalleatencion/', TipoDetalleAtencionApiView.as_view()),
    path('actualizar-tipodetalleatencion/<str:pk>', TipoDetalleAtencionToggleApiView.as_view()),
    path('registro-raza/', RazaApiView.as_view()),
    path('actualizar-raza/<str:pk>', RazaToggleApiView.as_view()),
]