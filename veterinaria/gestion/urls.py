from django.urls import path
from .views import EspecieApiView

urlpatterns = [
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('registro-especie/', EspecieApiView.as_view()),
]