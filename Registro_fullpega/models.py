from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Bicicleta(models.Model):
#     Nombre = models.CharField(max_length=120)
#     Modelo =  models.CharField(max_length=120)
#     Color =  models.CharField(max_length=120)
#     Aro =  models.CharField(max_length=120)
#     Estado =  models.CharField(max_length=120)
#     Tipo =  models.CharField(max_length=120)
#     Codigo =  models.CharField(max_length=120)
#     Monto_garantia = models.PositiveIntegerField()
#     Imagen = models.ImageField(upload_to='image')
#
class Cliente(models.Model):
    Nombre = models.CharField(max_length=120)
    Fecha_nacimiento = models.DateField()
    Email = models.EmailField()
    Direccion = models.CharField(max_length=60)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()
#
# class Reserva(models.Model):
#     pass
