# Generated by Django 2.0.4 on 2019-11-13 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0057_auto_20191113_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2019, 11, 13, 18, 2, 46, 316307)),
        ),
    ]
