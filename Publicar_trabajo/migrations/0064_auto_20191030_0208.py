# Generated by Django 2.0.4 on 2019-10-30 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0063_auto_20191030_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='Fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='historial_trabajo',
            name='Fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='Fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='postulantes',
            name='Fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='trabajo_acordado',
            name='Fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
