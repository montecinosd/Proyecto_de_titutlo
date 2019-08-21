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

def content_file_name(instance, filename):
    return '/'.join(['content', instance.Usuario.username, filename])
def content_file_document(instance, filename):
    return '/'.join(['document', instance.Usuario.username, filename])

class Areas(models.Model):
    Nombre = models.CharField(max_length=120)

class Direccion(models.Model):
    Comuna = models.CharField(max_length = 50, null=True,blank=True)
    Pais = models.CharField(max_length = 50, null=True,blank=True)
    Ciudad = models.CharField(max_length = 50,null=True,blank=True)
    Calle = models.CharField(max_length=100,null=True,blank=True)
    Numero_de_calle = models.CharField(max_length=100,null=True,blank=True)
class Persona(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length = 120,null=True,blank=True)
    Rut = models.CharField(max_length=20,null=True,blank=True)
    Imagen = models.ImageField(upload_to=content_file_name,null=True,blank=True)
    Telefono_C = models.CharField(max_length = 50,null=True,blank=True)
    Correo = models.CharField(max_length = 100,null=True,blank=True)
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    Fecha_nacimiento = models.CharField(max_length = 50,null=True,blank=True)



# class Reserva(models.Model):
#     pass
