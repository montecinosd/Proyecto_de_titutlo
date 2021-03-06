# Generated by Django 2.0.4 on 2019-09-12 02:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0018_auto_20190908_0222'),
        ('Publicar_trabajo', '0034_auto_20190908_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Hora', models.TimeField(default=datetime.datetime(2019, 9, 11, 23, 54, 33, 606368))),
                ('Postulante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro_fullpega.Persona')),
                ('Trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Trabajo')),
            ],
        ),
        migrations.AlterField(
            model_name='historial_trabajo',
            name='Hora',
            field=models.TimeField(default=datetime.datetime(2019, 9, 11, 23, 54, 33, 608159)),
        ),
    ]
