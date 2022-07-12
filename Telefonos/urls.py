from django.urls import path, include
from .views import home, inicio_sesion, consulta, telefonos, registro, agregar_telefono, modificar_telefono, eliminar_telefono, ubicacion, agregar_sucursal, modificar_sucursal, eliminar_sucursal, carrito, agregar_producto,eliminar_producto,limpiar_producto,restar_producto,comprar,historial_boleta,agregar_despacho,cambiar_en_camino,cambiar_enviado,seguimiento
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
    path('carrito', carrito, name='carrito'),
    path('agregar/<int:producto_id>/',agregar_producto,name="agregar_producto"),
    path('eliminar/<int:producto_id>/',eliminar_producto,name="eliminar_producto"),
    path('restar/<int:producto_id>/',restar_producto,name="restar_producto"),
    path('limpiar/',limpiar_producto,name="limpiar_producto"),
    path('historial',historial_boleta,name="historial"),
    path('comprar/',comprar,name="comprar"),
    path('despacho',agregar_despacho,name="despacho"),
    path('cambiar_en_camino/<num_b>',cambiar_en_camino,name="cambiar_en_camino"),
    path('cambiar_enviado/<num_b>',cambiar_enviado,name="cambiar_enviado"),
    path('seguimiento/<int:id_bol>/',seguimiento,name="seguimiento"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)