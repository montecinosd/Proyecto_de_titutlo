# Generated by Django 2.0.4 on 2019-09-18 07:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0037_auto_20190913_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo_acordado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Hora', models.TimeField(default=datetime.datetime(2019, 9, 18, 4, 0, 56, 279651))),
            ],
        ),
        migrations.AlterField(
            model_name='historial_trabajo',
            name='Hora',
            field=models.TimeField(default=datetime.datetime(2019, 9, 18, 4, 0, 56, 280585)),
        ),
        migrations.AlterField(
            model_name='postulantes',
            name='Hora',
            field=models.TimeField(default=datetime.datetime(2019, 9, 18, 4, 0, 56, 277804)),
        ),
        migrations.AddField(
            model_name='trabajo_acordado',
            name='postulante_acordado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Postulantes'),
        ),
    ]
