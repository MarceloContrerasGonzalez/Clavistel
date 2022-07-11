from django.shortcuts import render, redirect
import Telefonos
from Telefonos.Carrito import Carrito
from .models import Movil, Sucursal, Boleta, Despacho
from .forms import TelefonoForm, SucursalForm, DespachoForm, SignUpForm
import random


# Create your views here.
def home(request):
    return render(request,'Telefonos/index.html')

def inicio_sesion(request):
    return render(request,'Telefonos/inicio_sesion.html')

def consulta(request):
    return render(request,'Telefonos/Nesecitas_Ayuda.html')

def historial(request):
    return render(request,'Telefonos/historial.html')

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

def restar_stock(cantidad, id_telefono):
    compra = Movil.objects.get(id_movil = id_telefono)
    compra.cant -= cantidad
    compra.save()

def comprar(request):   
    productos = ''
    precio_total = 0
    cant = 0
    
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            restar_stock(int(value["cantidad"]),int(value["producto_id"]))
            cant += value["cantidad"]
            productos += value["nombre"] + ', '
            
            precio_total += value["acumulado"]
            
            nom_cli = request.user.username
            num_compra = random.randint(100000,999999)
        if request.user.is_staff == 1:
            precio_total = round(precio_total * 0.95)
        while Boleta.objects.filter(num_boleta=num_compra).exists():
            num_compra+=1
        else:
            Boleta.objects.create(num_boleta=num_compra, nom_cliente=str(nom_cli), estado=0, nom_productos=productos,cant_total=precio_total,cantidad=cant)
            
            limpiar_producto(request)
            return redirect("despacho")
    return redirect("carrito")

#historial

def historial_boleta(request):
    if request.user.is_authenticated and request.user.is_superuser == 1:
        listaBoleta = Boleta.objects.all()
        datos = {
            'historial_Boleta':listaBoleta
        }
    else:
        listaBoleta= Boleta.objects.filter(nom_cliente = request.user.username)
        datos = {
            'historial_Boleta':listaBoleta
        }
    return render (request,'Telefonos/historial.html',datos)    

# despacho

def despacho(request):
    return render(request,'Telefonos/despacho.html')

#agregar un despacho
def agregar_despacho(request):
    datos = {
        'despForm' : DespachoForm()
    }
    
    if (request.method == 'POST'):
        formulario = DespachoForm(request.POST)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Se ha añadido el despacho'
        else:
            datos['mensaje'] = 'Telefono NO se guardó'
  
    return render(request,'Telefonos/despacho.html', datos)


#cambiar estado a despachando...
def cambiar_en_camino(self, num_b): 
    boleta = Boleta.objects.get(num_boleta=num_b)
    boleta.estado = 1
    boleta.save()
    
    return redirect('historial')

#cambiar estado a despachado
def cambiar_enviado(self, num_b): 
    boleta = Boleta.objects.get(num_boleta=num_b)
    boleta.estado = 2
    boleta.save()
    
    return redirect('historial')

def seguimiento(request,id_bol):
    if request.user.is_authenticated and request.user.is_superuser == 1:
        listaSeguimiento = Boleta.objects.all()
        datos = {
            'listaSeguimiento':listaSeguimiento
        }
    else:
        listaSeguimiento = Boleta.objects.filter(num_boleta = id_bol) #compararlo con el numero de la boleta (fk)
        datos = {
            'listaSeguimiento':listaSeguimiento
        }
    return render (request,'Telefonos/seguimiento.html',datos)  

#antes que me muera, falta hacer que al generar un despacho, se autocomplete con el numero de la boleta del detalle recién linkeado,
#falta poder comparar el numero de la boleta del despacho con ese mismo numero de la boleta para ver su seguimiento,
#falta mostrar las horas de partida y llegada del paquete en el seguimiento del despacho, y también mostrar el estado en que se encuentra,
#falta hacer 2 funciones que cambien el estado a despachando y despachado, 
#creo que eso 