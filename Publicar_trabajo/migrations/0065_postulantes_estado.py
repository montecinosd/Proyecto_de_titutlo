# Generated by Django 2.0.4 on 2019-11-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0064_auto_20191030_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulantes',
            name='Estado',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
