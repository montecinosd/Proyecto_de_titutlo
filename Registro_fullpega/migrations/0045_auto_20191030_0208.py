# Generated by Django 2.0.4 on 2019-10-30 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0044_auto_20191030_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2019, 10, 30, 2, 8, 3, 535211)),
        ),
    ]
