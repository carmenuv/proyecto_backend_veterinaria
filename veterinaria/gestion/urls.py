from django.urls import path
from .views import EspecieApiView,EspecieToggleApiView,AnalisisApiView, AnalisisToggleApiView, TipoTrabajadorApiView,TipoTrabajadorToggleApiView

urlpatterns = [
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('registro-especie/', EspecieApiView.as_view()),
    path('actualizar-especie/<str:pk>', EspecieToggleApiView.as_view()),

    path('registro-analisis/', AnalisisApiView.as_view()),
    path('actualizar-analisis/<str:pk>', AnalisisToggleApiView.as_view()),

    path('registro-tipoTrabajador/', TipoTrabajadorApiView.as_view()),
    path('actualizar-tipoTrabajador/<str:pk>', TipoTrabajadorToggleApiView.as_view()),
]