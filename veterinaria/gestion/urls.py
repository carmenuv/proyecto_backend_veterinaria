from django.urls import path
from .views import EspecieApiView,EspecieToggleApiView, DiagnosticoApiView, DiagnosticoToggleApiView, ServicioApiView, ServicioToggleApiView

urlpatterns = [
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('registro-especie/', EspecieApiView.as_view()),
    path('actualizar-especie/<str:pk>', EspecieToggleApiView.as_view()),
    path('registro-diagnostico/', DiagnosticoApiView.as_view()),
    path('actualizar-diagnostico/<str:pk>', DiagnosticoToggleApiView.as_view()),
    path('registro-servicio/', ServicioApiView.as_view()),
    path('actualizar-servicio/<str:pk>', ServicioToggleApiView.as_view()),
]