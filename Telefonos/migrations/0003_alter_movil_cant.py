# Generated by Django 4.0.4 on 2022-07-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telefonos', '0002_alter_movil_cant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movil',
            name='cant',
            field=models.IntegerField(default=10, verbose_name='cantidad'),
        ),
    ]