# Generated by Django 4.0.4 on 2022-07-10 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Telefonos', '0007_despacho'),
    ]

    operations = [
        migrations.AddField(
            model_name='despacho',
            name='region',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='Telefonos.region'),
            preserve_default=False,
        ),
    ]
