# Generated by Django 2.0.4 on 2020-01-09 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0076_auto_20191225_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2020, 1, 9, 10, 58, 18, 663744)),
        ),
    ]
