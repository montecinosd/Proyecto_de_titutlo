# Generated by Django 2.0.4 on 2019-11-11 02:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0049_auto_20191110_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2019, 11, 10, 23, 54, 9, 543826)),
        ),
    ]
