from datetime import date,datetime
from Registro_fullpega.models import *

from django.db import models

def content_file_name(instance, filename):
    return '/'.join(['media/trabajo/', instance.Imagen, filename])
def content_file_document(instance, filename):
    return '/'.join(['document', instance.Usuario.username, filename])


class Trabajo(models.Model):
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE,blank=True, null=True)

    Nombre = models.CharField(max_length=120)
    Detalle = models.CharField(max_length=120)

    Monto_pago = models.PositiveIntegerField()
    Fecha = models.DateField()
    Hora = models.TimeField()
    rango_etario = models.CharField(
        max_length=20,
        choices=(
            ('Sin rango etario especifico', 'Sin rango etario especifico'),
            ('15-25', '15-25'),
            ('25-35', '25-35'),
            ('35-45', '35-45'),
            ('45-55', '45-55'),
            ('55-65', '55-65'),
            ),
        default='Sin rango etario especifico')
    Area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    Imagen = models.ImageField(upload_to="media", null=True, blank=True)
    Activo = models.PositiveIntegerField(default=1)

class Historial_trabajo(models.Model):
    Trabajo = models.OneToOneField(Trabajo,on_delete=models.CASCADE)
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Fecha = models.DateField(("Date"), default=date.today)
    Hora = models.TimeField(default=datetime.now())

# class Valoracion_trabajo(models.Model):
#     Trabajo = models.OneToOneField(Trabajo, on_delete=models.CASCADE)
#     Persona_trabajadora = models.ForeignKey(Persona, on_delete=models.CASCADE)
#     Persona_publicadora = models.ForeignKey(Persona, on_delete=models.CASCADE)

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
