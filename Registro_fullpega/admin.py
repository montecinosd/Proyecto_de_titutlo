from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pk','Usuario','Nombre','Rut','Imagen','Telefono_C','Correo','Direccion')


    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
                         % (obj.picture.url))

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('Comuna','Pais','Ciudad','Calle','Numero_de_calle')

@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)

