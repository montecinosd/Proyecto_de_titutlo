# Generated by Django 2.0.4 on 2019-09-27 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0033_auto_20190927_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2019, 9, 27, 1, 14, 21, 684623)),
        ),
    ]