# Generated by Django 2.0.4 on 2019-08-06 01:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0009_auto_20190806_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='Direccion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Registro_fullpega.Direccion'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='Hora',
            field=models.TimeField(default=datetime.datetime(2019, 8, 6, 1, 13, 59, 974582)),
        ),
    ]
