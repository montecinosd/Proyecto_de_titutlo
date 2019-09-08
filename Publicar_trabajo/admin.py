from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('pk','Usuario','Nombre','Detalle','Monto_pago','Fecha','Hora','rango_etario','Area','Direccion',"Activo")


    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
                         % (obj.picture.url))

@admin.register(Historial_trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('Persona','Trabajo','Fecha','Hora',)


    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
                         % (obj.picture.url))
