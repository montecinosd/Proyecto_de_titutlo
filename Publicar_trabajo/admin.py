from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('Usuario','Nombre','Detalle','Monto_pago','Fecha','Hora','rango_etario','Area','Direccion','Imagen')


    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
                         % (obj.picture.url))
