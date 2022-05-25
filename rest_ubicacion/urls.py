from django.urls import path
from rest_ubicacion.views import lista_sucursales

urlpatterns = [
    path('lista_sucursales',lista_sucursales, name="lista_sucursales"),
]
