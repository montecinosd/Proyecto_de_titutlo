# Generated by Django 2.0.4 on 2019-10-04 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0056_notificaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_trabajo',
            name='Trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Trabajo'),
        ),
    ]
