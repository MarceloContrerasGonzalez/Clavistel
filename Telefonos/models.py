from django.db import models

# TABLA Marca.
class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True,verbose_name='id_marca')
    nom_marca = models.CharField(max_length=100,verbose_name='Marca')

    def __str__(self):
        return self.nom_marca
    
# TABLA TipoEnvio.
class TipoEnvio(models.Model):
    idTipoEnvio = models.IntegerField(primary_key=True,verbose_name='id_tipo_envio')
    tipoEnvio = models.CharField(max_length=50,verbose_name='tipo_envio')

    def __str__(self):
        return self.tipoEnvio    

# TABLA Movil.
class Movil(models.Model):
    id_movil = models.IntegerField(primary_key=True,verbose_name='id_movil')
    img = models.ImageField(upload_to='Telefonos/static/Telefonos/img/imgdjango',verbose_name='img')
    costo = models.IntegerField(verbose_name='precio')
    descripcion = models.CharField(max_length=100,verbose_name='descripcion')
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    id_tipo_envio = models.ForeignKey(TipoEnvio, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


    
