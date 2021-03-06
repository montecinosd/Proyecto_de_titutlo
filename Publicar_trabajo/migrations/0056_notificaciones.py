# Generated by Django 2.0.4 on 2019-10-04 18:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0037_auto_20191004_1551'),
        ('Publicar_trabajo', '0055_historial_trabajo_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('Hora', models.TimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('Activo', models.PositiveIntegerField(default=1)),
                ('Trabajo_acordado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Trabajo_acordado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro_fullpega.Persona')),
            ],
        ),
    ]
