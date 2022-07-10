from django.contrib import admin
from .models import Movil, Marca, TipoEnvio, Sucursal, Region, Boleta

# Register your models here.
admin.site.register(Movil)
admin.site.register(Marca)
admin.site.register(TipoEnvio)
admin.site.register(Sucursal)
admin.site.register(Region)
admin.site.register(Boleta)
