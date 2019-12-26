# Generated by Django 2.0.4 on 2019-12-25 21:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0075_auto_20191225_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferencias',
            name='Mireccion',
        ),
        migrations.AddField(
            model_name='preferencias',
            name='Comuna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro_fullpega.Comuna'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2019, 12, 25, 18, 20, 35, 358465)),
        ),
    ]
