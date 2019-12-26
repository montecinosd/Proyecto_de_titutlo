from django.db import models
from django.contrib.auth.models import User
from datetime import *
from django.utils import timezone
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

def content_file_name(instance, filename):
    return '/'.join(['content', instance.Usuario.username, filename])
def content_file_document(instance, filename):
    return '/'.join(['document', instance.Usuario.username, filename])

class Areas(models.Model):
    Nombre = models.CharField(max_length=120)

class Region(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    def add_commune(self, name):
        return Comuna.objects.create(name=nombre,
                                      region=self)


class Comuna(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)




class Persona(models.Model):
    Usuario = models.ForeignKey(User,primary_key=True, on_delete=models.CASCADE)

    Nombre = models.CharField(max_length = 120,null=True,blank=True)
    Rut = models.CharField(max_length=20,null=True,blank=True)
    Imagen = models.ImageField(upload_to="media",null=True,blank=True)
    Telefono_C = models.CharField(max_length = 50,null=True,blank=True)
    Correo = models.CharField(max_length = 100,null=True,blank=True)
    # Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    Fecha_nacimiento = models.DateField(default=datetime.now())
    # edad = models.DateField()
    Facebook = models.CharField(max_length = 120,null=True,blank=True)
    Twitter = models.CharField(max_length = 120,null=True,blank=True)
    Linkedin = models.CharField(max_length = 120,null=True,blank=True)
    Instagram = models.CharField(max_length = 120,null=True,blank=True)
    Puntaje_watson = models.IntegerField(default=0)
    Label_watson = models.CharField(max_length = 120,null=True,blank=True)
    Estrellas = models.CharField(max_length = 120,null=True,blank=True)
    Descripcion_propia = models.TextField()
    #1 sin privilegios, 2 dual, 3 publicar, 4 buscar
    privilegios = models.IntegerField(default=1)
    Fecha_registro = models.DateTimeField(default=datetime.now)



    @property
    def Direccion(self):
        return Direccion.objects.filter(Persona = self).get(Principal = 1)



class Direccion(models.Model):
    Comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True,blank=True)
    # Pais = models.CharField(max_length = 50, null=True,blank=True)
    # Ciudad = models.CharField(max_length = 50,null=True,blank=True)
    Calle = models.CharField(max_length=100,null=True,blank=True)
    Numero_de_calle = models.CharField(max_length=100,null=True,blank=True)
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Principal = models.IntegerField(default=1)

    def apagar_principal(self):
        self.Principal = 0
    def establecer_principal(self):
        self.Principal = 1

class Preferencias(models.Model):
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    M_minimo = models.IntegerField(default=1)
    M_maximo = models.IntegerField(default=1000000000)
    Comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True, blank=True)
    Area = models.ForeignKey(Areas,on_delete=models.CASCADE, null=True, blank=True)
    Fecha_registro = models.DateTimeField(default=datetime.now)

    # Activo = models.

class Historico_watson(models.Model):
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Puntaje = models.IntegerField(default=0)
    Label = models.CharField(max_length = 120,null=True,blank=True)
    Fecha = models.DateField(default=datetime.now, null=True, blank=True)
    Hora = models.TimeField(default=datetime.now, null=True, blank=True)









# class Reserva(models.Model):
#     pass
