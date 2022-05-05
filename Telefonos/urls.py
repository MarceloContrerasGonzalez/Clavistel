from django.urls import path
from .views import home, login, consulta, telefonos, registro

urlpatterns =[
    path('', home, name="home"),
    path('login', login, name="login"),
    path('consulta', consulta, name="consulta"),
    path('telefonos', telefonos, name="telefonos"),
    path('registro', registro, name="registro")
]