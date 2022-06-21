from  django import forms
from django.forms import ModelForm
from .models import Movil, Sucursal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TelefonoForm(ModelForm):
    class Meta:
        model = Movil
        fields = ['id_movil','nombre','img','costo','marca','tipo_envio']
        
class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['id_sucursal','nombre_sucursal','direccion','region']
        
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=25, label='Usuario' ,help_text='Ingrese su Usuario.')
    email = forms.EmailField(max_length=254, label='Correo' ,help_text='Ingrese un correo.')
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput , label='Contraseña' ,help_text='Ingrese una Contraseña valida.')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput , label='Contraseña' ,help_text='Ingrese Nuevamente Su Contraseña.')
    is_staff = forms.BooleanField(required=False, label='Admin')
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2','is_staff')