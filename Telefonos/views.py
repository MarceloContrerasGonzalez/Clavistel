from itertools import product
import re
from django.shortcuts import render, redirect
import Telefonos
from Telefonos.Carrito import Carrito
from .models import Movil, Sucursal
from .forms import TelefonoForm, SucursalForm, SignUpForm


# Create your views here.
def home(request):
    return render(request,'Telefonos/index.html')

def inicio_sesion(request):
    return render(request,'Telefonos/inicio_sesion.html')

def consulta(request):
    return render(request,'Telefonos/Nesecitas_Ayuda.html')

def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')
    else:
        form = SignUpForm()
    return render(request,'Telefonos/registro.html', {'form': form})


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



''' API SUCURSALES '''



def ubicacion(request):
    lista_Sucursal = Sucursal.objects.all()
    datos = {
        'lista_Sucursal' : lista_Sucursal
    }
    return render(request,'Telefonos/ubicacion.html', datos)


def agregar_sucursal(request):
    datos = {
        'sucform' : SucursalForm()
    }
    
    if (request.method == 'POST'):
        formulario = SucursalForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Se ha añadido la Sucursal'
        else:
            datos['mensaje'] = 'NO se ha añadido la Sucursal'
  
    return render(request,'Telefonos/agregar_sucursal.html', datos)

def modificar_sucursal(request, id):
    sucursal = Sucursal.objects.get(id_sucursal=id)
    
    datos = {
        'sucform':SucursalForm(instance=sucursal)
    }
    
    if (request.method == 'POST'):
        formulario = SucursalForm(request.POST, request.FILES, instance=sucursal)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Telefono modificado correctamente'
        else:
            datos['mensaje'] = 'Telefono NO se modifico'
    
    return render(request,'Telefonos/modificar_sucursal.html', datos)

def eliminar_sucursal(request,id):
    sucursal = Sucursal.objects.get(id_sucursal=id)
    sucursal.delete()

    return redirect(to='ubicacion')

#carrito

def carrito(request):
    productos = Movil.objects.all()
    return render(request,'Telefonos/carrito.html', {'telefonos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Movil.objects.get( id_movil=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Movil.objects.get(id_movil=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Movil.objects.get(id_movil=producto_id)
    carrito.restar(producto)
    return redirect('carrito')

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')

def guardar_carrito(request):
    carrito = Carrito(request)
    carrito.guardar_carrito()
    return redirect('carrito')

def restar_stock (cantidad,telefono_id):
    compra = Movil.objects.get(id_movil= telefono_id)
    compra.cant -= cantidad
    compra.save()
    
def comprar(request):
    if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                restar_stock(int(value["cantidad"]), int(value["producto_id"]))
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")
                
    

