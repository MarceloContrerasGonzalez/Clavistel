# Generated by Django 4.0.4 on 2022-07-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telefonos', '0005_boleta_cant_total_boleta_nom_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='cantidad',
            field=models.IntegerField(default=5, verbose_name='Cantidades'),
        ),
    ]