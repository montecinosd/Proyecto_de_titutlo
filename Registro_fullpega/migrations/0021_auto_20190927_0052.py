# Generated by Django 2.0.4 on 2019-09-27 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0020_auto_20190927_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]