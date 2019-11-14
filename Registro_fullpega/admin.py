from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pk','Usuario','Nombre','Rut','Imagen','Telefono_C','Correo','Fecha_nacimiento','Facebook','Twitter','Linkedin','Instagram','privilegios', 'Puntaje_watson','Label_watson')


    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
                         % (obj.picture.url))

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('Comuna','Calle','Numero_de_calle','Persona','Principal')

@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    list_display = ('pk','Nombre',)

