from django.urls import path, include
from .views import home, inicio_sesion, consulta, telefonos, registro, agregar_telefono, modificar_telefono, eliminar_telefono, ubicacion, agregar_sucursal, modificar_sucursal, eliminar_sucursal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', home, name='home'),
    path('inicio_sesion', inicio_sesion, name='inicio_sesion'),
    path('consulta', consulta, name='consulta'),
    path('telefonos', telefonos, name='telefonos'),
    path('registro', registro, name='registro'),
    path('agregar', agregar_telefono, name='agregar'),
    path('modificar/<id>', modificar_telefono, name='modificar'),
    path('eliminar/<id>', eliminar_telefono, name='eliminar'),
    path('ubicacion', ubicacion, name='ubicacion'),
    path('api/', include('rest_ubicacion.urls')),
    path('agregar_sucursal',agregar_sucursal,name="agregar_sucursal"),
    path('modificar_sucursal/<id>',modificar_sucursal,name="modificar_sucursal"),
    path('eliminar_sucursal/<id>',eliminar_sucursal,name="eliminar_sucursal"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)