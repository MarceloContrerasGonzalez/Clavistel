from django.db import models

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
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo_envio = models.ForeignKey(TipoEnvio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


    
