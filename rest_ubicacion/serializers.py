from rest_framework import serializers
from Telefonos.models import Sucursal

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal  
        fields = ['id_sucursal', 'img', 'nombre_sucursal', 'direccion', 'region']