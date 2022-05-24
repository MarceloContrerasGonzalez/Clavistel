from django.urls import path
from rest_ubicacion.views import lista_telefonos

urlpatterns = [
    path('lista_telefonos',lista_telefonos, name= "lista_telefonos"),
]
