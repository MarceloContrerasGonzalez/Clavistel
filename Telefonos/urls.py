from django.urls import path, include
from .views import historial, home, inicio_sesion, consulta, telefonos, registro, agregar_telefono, modificar_telefono, eliminar_telefono, ubicacion, agregar_sucursal, modificar_sucursal, eliminar_sucursal, carrito, historial
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', home, name='home'),
    path('inicio_sesion', inicio_sesion, name='inicio_sesion'),
    path('consulta', consulta, name='consulta'),
    path('telefonos', telefonos, name='telefonos'),
    path('registro', registro, name='registro'),
    path('agregar', agregar_telefono, name='agregar'),
    path('carrito', carrito, name='carrito'),
    path('historial', historial, name='historial'),
    path('modificar/<id>', modificar_telefono, name='modificar'),
    path('eliminar/<id>', eliminar_telefono, name='eliminar'),
    path('ubicacion', ubicacion, name='ubicacion'),
    path('api/', include('rest_ubicacion.urls')),
    path('agregar_sucursal',agregar_sucursal,name="agregar_sucursal"),
    path('modificar_sucursal/<id>',modificar_sucursal,name="modificar_sucursal"),
    path('eliminar_sucursal/<id>',eliminar_sucursal,name="eliminar_sucursal"),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(),name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)