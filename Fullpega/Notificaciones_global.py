
from Publicar_trabajo.models import *
from Registro_fullpega.models import *
from Auth_fullpega.models import *

def get_notificaciones(request):
    # data = {}
    #si no hay usuario
    try:
        if(request.user.pk == None):
            return ""
        else:
            usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
            # data['usuario_solicitud'] = usuario_solicitud
            notificaciones = Notificaciones.objects.filter(usuario=usuario_solicitud).exclude(Activo = 0).order_by('-Fecha')
            # for i in notificaciones:
                # print(i.Activo)
            notificaciones_contables = Notificaciones.objects.filter(usuario = usuario_solicitud).exclude(Activo = 0).exclude(Contable = 0)

            data = {}
            print("hola")
            data['notificaciones'] = notificaciones
            data['notificaciones_contables'] = notificaciones_contables
            return data
    except:
        print("except notis")
        return ""

# def apagar_notificaciones(request):
#     print("apagar_notis xdxdxd")
#     try:
#         print("holaasdasdaa")
#         if (request.user.pk == None):
#             return ""
#         else:
#             print("desactivando notis")
#             usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
#             notificaciones_contables = Notificaciones.objects.filter(usuario=usuario_solicitud).exclude(Activo=0).exclude(Contable=0)
#             for i in notificaciones_contables:
#                 i.apagar_contable()
#                 i.save()
#     except:
#         print("except apagar notis")
#         return ""


