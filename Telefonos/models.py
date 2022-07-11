from django.db import models
from datetime import datetime, timedelta

# Tablas Telefonos

# TABLA Marca.
class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True,verbose_name='id marca')
    nom_marca = models.CharField(max_length=100,verbose_name='Marca')

    def __str__(self):
        return self.nom_marca
    
# TABLA TipoEnvio.
class TipoEnvio(models.Model):
    idTipoEnvio = models.AutoField(primary_key=True,verbose_name='id envio')
    tipoEnvio = models.CharField(max_length=50,verbose_name='tipo de envio')

    def __str__(self):
        return self.tipoEnvio    

# TABLA Movil.
class Movil(models.Model):
    id_movil = models.AutoField(primary_key=True,verbose_name='id movil')
    img = models.ImageField(upload_to='Telefonos/static/Telefonos/img/imgdjango',verbose_name='imagen')
    costo = models.IntegerField(verbose_name='precio')
    nombre = models.CharField(max_length=100,verbose_name='Nombre Celular')
    cant = models.IntegerField(default=10, verbose_name='cantidad')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo_envio = models.ForeignKey(TipoEnvio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

''' ---------------------------------------------------------------------------------- '''
#Tablas Sucursal

# TABLA Region.
class Region(models.Model):
    id_region = models.AutoField(primary_key=True,verbose_name='id Región')
    nombre_region = models.CharField(max_length=50,verbose_name='Nombre Región')

    def __str__(self):
        return self.nombre_region

# TABLA Sucursal.
class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True,verbose_name='Código Sucursal')
    nombre_sucursal = models.CharField(max_length=100,verbose_name='Nombre Sucursal')
    direccion = models.CharField(max_length=100,verbose_name='Dirección')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_sucursal

#Tablas Carrito


def HoraPreparacion():
    return datetime.today() + timedelta(hours=16)

def HoraDespacho():
    return datetime.today() + timedelta(hours=34)


class Boleta(models.Model):
    num_boleta = models.AutoField(primary_key=True,verbose_name='Código Boleta')
    nom_cliente = models.CharField(max_length=50,verbose_name='Nombre Cliente')
    estado = models.IntegerField(default=0, verbose_name="Estado")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    fechaPreparacion = models.DateTimeField(default=HoraPreparacion, verbose_name="Fecha")
    fechaDespacho = models.DateTimeField(default=HoraDespacho, verbose_name="Fecha")
    nom_productos = models.CharField(max_length=250,verbose_name='Productos')
    cant_total = models.IntegerField(verbose_name='Cantidad total')
    cantidad = models.IntegerField(default=5, verbose_name='Cantidades')
    
    def __str__(self):
        return str(self.num_boleta)
    

class Despacho(models.Model):
    id_despacho = models.AutoField(primary_key=True,verbose_name='Número Despacho')
    nom_destinatario = models.CharField(max_length=250,verbose_name='Nombre Destinatario')
    direccion =  models.CharField(max_length=250,verbose_name='Dirección')
    num_casa = models.IntegerField(default=450, verbose_name="Número de la casa/depa")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    num_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_despacho)
    