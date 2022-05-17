from django.contrib import admin
from .models import Movil, Marca, TipoEnvio

# Register your models here.
admin.site.register(Movil)
admin.site.register(Marca)
admin.site.register(TipoEnvio)
