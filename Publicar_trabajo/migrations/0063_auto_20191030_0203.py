# Generated by Django 2.0.4 on 2019-10-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0062_notificaciones_trabajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='Fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
