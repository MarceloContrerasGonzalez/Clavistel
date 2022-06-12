from django.urls import path
from rest_ubicacion.views import lista_sucursales, detalle_sucursal
from rest_ubicacion.viewsLogin import login

urlpatterns = [
    path('lista_sucursales',lista_sucursales, name="lista_sucursales"),
    path('detalle_sucursal/<idSuc>',detalle_sucursal, name="detalle_sucursal"),
    path('login',login, name="login"),
]
