# Generated by Django 2.0.4 on 2019-09-27 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0052_auto_20190927_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='historial_trabajo',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='postulantes',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='trabajo_acordado',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]