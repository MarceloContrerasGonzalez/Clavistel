from  django import forms
from django.forms import ModelForm
from .models import Movil, Sucursal, Despacho
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TelefonoForm(ModelForm):
    class Meta:
        model = Movil
        fields = ['id_movil','nombre','img','costo','marca','tipo_envio','cant']
        
class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['id_sucursal','nombre_sucursal','direccion','region']

class DespachoForm(ModelForm):
    class Meta:
        model = Despacho
        fields = ['id_despacho','nom_destinatario','direccion','num_casa','region','num_boleta']
        
class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ('Las contraseñas deben ser iguales'),
    }

    username = forms.CharField(max_length=25, label='Usuario' ,help_text='Ingrese su Usuario.', error_messages={'unique': 'Este usuario ya existe'})
    email = forms.EmailField(max_length=254, label='Correo' ,help_text='Ingrese un correo.', error_messages={'invalid': 'Correo Invalido'})
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput , label='Contraseña', help_text='Ingrese una Contraseña valida.')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput , label='Contraseña', help_text='Ingrese Nuevamente Su Contraseña.')
    
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2','is_staff') 