from django.shortcuts import render, redirect
from .models import Movil, Sucursal
from .forms import TelefonoForm

# Create your views here.
def home(request):
    return render(request,'Telefonos/index.html')

def login(request):
    return render(request,'login/login.html')

def consulta(request):
    return render(request,'consulta/Nesecitas_Ayuda.html')

def registro(request):
    return render(request,'registro/registro.html')

def ubicacion(request):
    lista_Sucursal = Sucursal.objects.all()
    datos = {
        'lista_Sucursal' : lista_Sucursal
    }
    return render(request,'rest_ubicacion/ubicacion.html', datos)

def telefonos(request):
    lista_Movil = Movil.objects.all()
    datos = {
        'lista_Movil' : lista_Movil
    }
    return render(request,'Telefonos/Phones.html', datos)

def agregar_telefono(request):
    datos = {
        'form' : TelefonoForm()
    }
    
    if (request.method == 'POST'):
        formulario = TelefonoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Telefono se guardó'
        else:
            datos['mensaje'] = 'Telefono NO se guardó'
  
    return render(request,'Telefonos/agregar_telefono.html', datos)

def modificar_telefono(request, id):
    movil = Movil.objects.get(id_movil=id)
    
    datos = {
        'form':TelefonoForm(instance=movil)
    }
    
    if (request.method == 'POST'):
        formulario = TelefonoForm(request.POST, request.FILES, instance=movil)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Telefono modificado correctamente'
        else:
            datos['mensaje'] = 'Telefono NO se modifico'
    
    return render(request,'Telefonos/modificar_telefono.html', datos)

def eliminar_telefono(request, id):
    movil = Movil.objects.get(id_movil=id)
    movil.delete()
    
    return redirect(to= 'telefonos')