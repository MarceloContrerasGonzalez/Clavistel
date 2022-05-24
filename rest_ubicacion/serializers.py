import imp
from rest_framework import serializers
from Telefonos.models import Movil

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movil
        fields = ['id_movil','nombre','img','costo','marca','tipo_envio']