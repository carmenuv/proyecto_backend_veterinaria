from django.urls import path
from .views import EspecieApiView,EspecieToggleApiView,EspecieActualizarApiView

urlpatterns = [
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('registro-especie/', EspecieApiView.as_view()),
    path('actualizar-especie/<str:EspecieId>', EspecieToggleApiView.as_view()),
    path('actualizar-especies/<str:pk>', EspecieActualizarApiView.as_view()),
]