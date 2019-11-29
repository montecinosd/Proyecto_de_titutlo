# Generated by Django 2.0.4 on 2019-11-28 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0065_postulantes_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='Fecha_publicacion',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='Fecha_vencimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='Hora_publicacion',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
