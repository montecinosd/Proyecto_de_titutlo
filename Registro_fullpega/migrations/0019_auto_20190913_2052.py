# Generated by Django 2.0.4 on 2019-09-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0018_auto_20190908_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Fecha_nacimiento',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
    ]
