# Generated by Django 2.0.4 on 2019-08-05 05:13

import Registro_fullpega.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registro_fullpega', '0007_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('Rut', models.CharField(blank=True, max_length=20, null=True)),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to=Registro_fullpega.models.content_file_name)),
                ('Telefono_C', models.CharField(blank=True, max_length=50, null=True)),
                ('Correo', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Areas_interes',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='Block_depto',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='calle',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='numero',
        ),
        migrations.AddField(
            model_name='direccion',
            name='Calle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='Ciudad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='Comuna',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='Numero_de_calle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='Pais',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AddField(
            model_name='persona',
            name='Direccion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Registro_fullpega.Direccion'),
        ),
        migrations.AddField(
            model_name='persona',
            name='Usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
