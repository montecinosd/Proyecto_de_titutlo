from django.db import models
from datetime import date
# Create your models here.

class Trabajo(models.Model):

    Nombre = models.CharField(max_length=120)
    Detalle = models.CharField(max_length=120)

    Monto_pago = models.PositiveIntegerField()
    Fecha = models.DateField(("Date"), default=date.today)
    Hora = models.TimeField()
    rango_etario = models.CharField(
        max_length=4,
        choices=(
            ('Sin rango etario especifico', 'Sin rango etario especifico'),
            ('15-25', '15-25'),
            ('25-35', '25-35'),
            ('35-45', '35-45'),
            ('45-55', '45-55'),
            ('55-65', '55-65'),
            ),
        default='Sin rango etario especifico')
    Area = models.CharField(max_length=120)
    Direccion = models.CharField(max_length=120)

   #  Email = models.EmailField()
   #  Direccion = models.CharField(max_length=60)
   #  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
   #
   #  rut = models.CharField(max_length=8)
   #  dv =
   #  #privilegios 0 usuario normal, 1 oferente, 2 postulante, 3 mutual
   # # privilegio = models.PositiveIntegerField(default=0)
   #  privilegio = models.CharField(
   #      max_length=4,
   #      choices=(
   #          ('Sp', 'Sin_privilegios'),
   #          ('Po', 'Privilegio_ofrecer'),
   #          ('Pp', 'Privilegio_publicar'),
   #          ('Pm', 'Privilegio_mutuo'),),
   #      default='Sp')
   #  #Areas de interes
   #  Areas_interes = models.ForeignKey(Areas, on_delete=models.CASCADE, default=None, blank=True, null=True)