from django.urls import path
from .views import home, login, consulta, telefonos, registro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', home, name="home"),
    path('login', login, name="login"),
    path('consulta', consulta, name="consulta"),
    path('telefonos', telefonos, name="telefonos"),
    path('registro', registro, name="registro")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)