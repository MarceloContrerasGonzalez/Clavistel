from  django import forms
from django.forms import ModelForm
from .models import Movil, Sucursal

class TelefonoForm(ModelForm):
    class Meta:
        model = Movil
        fields = ['id_movil','nombre','img','costo','marca','tipo_envio']
        
class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['id_sucursal','nombre_sucursal','direccion','region']