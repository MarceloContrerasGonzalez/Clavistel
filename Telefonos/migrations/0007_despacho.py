# Generated by Django 4.0.4 on 2022-07-10 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telefonos', '0006_boleta_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id_despacho', models.AutoField(primary_key=True, serialize=False, verbose_name='Número Despacho')),
                ('nom_destinatario', models.CharField(max_length=250, verbose_name='Nombre Destinatario')),
                ('direccion', models.CharField(max_length=250, verbose_name='Dirección')),
            ],
        ),
    ]
