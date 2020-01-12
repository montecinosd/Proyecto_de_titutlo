from datetime import *
from datetime import timedelta
from Registro_fullpega.models import *
import time
from datetime import datetime, date, time, timedelta

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
    Fecha = models.DateTimeField(null=True, blank=True)

    Hora = models.TimeField(null=True, blank=True)
    Fecha_publicacion = models.DateTimeField(default=datetime.now)
    Hora_publicacion = models.TimeField(default=datetime.now)
    Fecha_vencimiento = models.DateTimeField(null=True, blank=True)
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
    Personas_requeridas = models.PositiveIntegerField(default=1)
    Vacantes = models.PositiveIntegerField(default=1)
    Activo = models.PositiveIntegerField(default=1)

    # def fecha_vencimiento(self):
    #     return self.Fecha_publicacion + datetime.timedelta(days=2)
    #postulantes a una trabajo debe hacerse un filter
class Postulantes(models.Model):
    Trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    Postulante = models.ForeignKey(Persona,on_delete=models.CASCADE)
    Fecha = models.DateTimeField(default=datetime.now)
    Hora = models.TimeField(default=datetime.now)
    #0 no aceptado, 1 aceptado, 2 cancelado(?)
    Estado = models.PositiveIntegerField(default=0)

#model de historial de traajos acordados activos o pasados, estos se realizaron y se aceptaron con distinta fecha y hora que cuando se postula
class Trabajo_acordado(models.Model):
    #aqui se tiene el trabajo que se postula, el usuario ( atraves del trabajo) y el postulante - se desvia la redundancia
    postulante_acordado = models.ForeignKey(Postulantes, on_delete=models.CASCADE)
    Fecha = models.DateField(default=datetime.now, null=True, blank=True)
    Hora = models.TimeField(default=datetime.now, null=True, blank=True)

class Calificaciones(models.Model):
    usuario = models.ForeignKey(Persona, on_delete=models.CASCADE,related_name='usuario')
    usuario_calificador = models.ForeignKey(Persona, on_delete=models.CASCADE,related_name='usuario_calificador')
    Pega_calificada = models.ForeignKey(Trabajo,on_delete=models.CASCADE)
    Estrellas = models.PositiveIntegerField(null=True, blank=True)
    Comentarios = models.CharField(max_length=120, null=True, blank=True)
    Fecha = models.DateField(default=datetime.now, null=True, blank=True)
    Hora = models.TimeField(default=datetime.now, null=True, blank=True)
    Realizada = models.PositiveIntegerField(default=0)

class Historial_trabajo(models.Model):
    Trabajo = models.ForeignKey(Trabajo,on_delete=models.CASCADE)
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Fecha = models.DateField(default=datetime.now)
    Hora = models.TimeField(default=datetime.now)
    #1 publicar 2 realizar
    tipo = models.PositiveIntegerField(default=1)

class Notificaciones(models.Model):
    usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Fecha = models.DateField(default=datetime.now, null=True, blank=True)
    Hora = models.TimeField(default=datetime.now, null=True, blank=True)
    Activo = models.PositiveIntegerField(default=1)

    Trabajo_acordado = models.ForeignKey(Trabajo_acordado, on_delete=models.CASCADE,null=True, blank=True)
    Trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE,null=True, blank=True)
    # 1 = calificacion, 2 = alerta de aceptar postulante, 3 = de nuevo postulante
    Tipo = models.PositiveIntegerField(default=1)
    Contable = models.PositiveIntegerField(default=1)

    def apagar_contable(self):
        self.Contable = 0

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
