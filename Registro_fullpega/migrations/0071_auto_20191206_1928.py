# Generated by Django 2.0.4 on 2019-12-06 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0070_auto_20191202_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='Descripcion_propia',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2019, 12, 6, 19, 27, 5, 851261)),
        ),
    ]
