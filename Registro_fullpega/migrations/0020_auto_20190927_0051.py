# Generated by Django 2.0.4 on 2019-09-27 03:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0019_auto_20190913_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]