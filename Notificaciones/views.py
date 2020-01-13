from django.shortcuts import render

# Create your views here.
def apagar_notificaciones(request):
    if (request.GET):
        print("HOAXDASDASDJ")
    print("apagar_notis xdxdxd")
    try:
        print("holaasdasdaa")
        if (request.user.pk == None):
            print("ctm")
        else:
            print("desactivando notis")
            usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
            notificaciones_contables = Notificaciones.objects.filter(usuario=usuario_solicitud).exclude(Activo=0).exclude(Contable=0)
            for i in notificaciones_contables:
                i.apagar_contable()
                i.save()
    except:
        print("except apagar notis")
        return ""
