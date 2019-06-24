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


class Areas(models.Model):
    Nombre = models.CharField(max_length=120)

class Cliente(models.Model):

    Nombre = models.CharField(max_length=120)
    Fecha_nacimiento = models.DateField()
    Email = models.EmailField()
    Direccion = models.CharField(max_length=60)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()
    #privilegios 0 usuario normal, 1 oferente, 2 postulante, 3 mutual
   # privilegio = models.PositiveIntegerField(default=0)
    privilegio = models.CharField(
        max_length=4,
        choices=(
            ('Sp', 'Sin_privilegios'),
            ('Po', 'Privilegio_ofrecer'),
            ('Pp', 'Privilegio_publicar'),
            ('Pm', 'Privilegio_mutuo'),),
        default='Sp')
    #Areas de interes
    Areas_interes = models.ForeignKey(Areas, on_delete=models.CASCADE, default=None, blank=True, null=True)

class Direccion(models.Model):
    calle = models.CharField(max_length=120)
    comuna = models.CharField(max_length=120)
    numero = models.PositiveIntegerField()
    Pais = models.CharField(max_length=120)
    Block_depto = models.CharField(max_length=120)


# class Reserva(models.Model):
#     pass
