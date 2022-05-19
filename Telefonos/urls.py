from django.urls import path
from .views import home, login, consulta, telefonos, registro, agregar_telefono, modificar_telefono, eliminar_telefono
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', home, name='home'),
    path('login', login, name='login'),
    path('consulta', consulta, name='consulta'),
    path('telefonos', telefonos, name='telefonos'),
    path('registro', registro, name='registro'),
    path('agregar', agregar_telefono, name='agregar'),
    path('modificar/<id>', modificar_telefono, name='modificar'),
    path('eliminar/<id>', eliminar_telefono, name='eliminar')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)