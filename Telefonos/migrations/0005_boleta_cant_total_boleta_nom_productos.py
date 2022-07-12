# Generated by Django 4.0.4 on 2022-07-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telefonos', '0004_boleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='cant_total',
            field=models.IntegerField(default=10, verbose_name='Cantidad total'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boleta',
            name='nom_productos',
            field=models.CharField(default='Celularesss', max_length=250, verbose_name='Productos'),
            preserve_default=False,
        ),
    ]
