# Generated by Django 2.0.4 on 2019-09-27 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0050_auto_20190927_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='Fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='calificaciones',
            name='Hora',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='postulantes',
            name='Fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='postulantes',
            name='Hora',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='trabajo_acordado',
            name='Fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='trabajo_acordado',
            name='Hora',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]