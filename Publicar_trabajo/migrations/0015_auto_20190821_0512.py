# Generated by Django 2.0.4 on 2019-08-21 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0014_auto_20190821_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='Hora',
            field=models.TimeField(default=datetime.datetime(2019, 8, 21, 5, 12, 35, 164724)),
        ),
    ]