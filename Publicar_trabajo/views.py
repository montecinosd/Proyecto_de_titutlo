from django.shortcuts import render
# from Registro_fullpega.models import *
# from Registro_fullpega.forms import *
from Publicar_trabajo.models import *
from Publicar_trabajo.forms import *
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User

def handle_uploaded_file(f):
    print(f)
    with open('media/'+f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def validar_trabajos(trabajos):
    try:
        fecha_actual = timezone.now()
        print(fecha_actual)
        for i in trabajos:
            print (i.Fecha_vencimiento)
            if( i.Fecha_vencimiento < fecha_actual):
                print("se paso")
                if(i.Activo ==0):
                    pass
                i.Activo = 2
                i.save()
                print(i.Activo)
            else:
                print("esta dentro")
    except:
        print("error")
# Create your views here.
@login_required(login_url='/auth/login')
def publicar_trabajo(request,pk_user):
    data = {}

    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    areas = Areas.objects.all()
    usuario = Persona.objects.filter(Usuario=pk_user)
    print(usuario)
    data['usuario'] = usuario
    data['areas'] = areas
    data['form'] = TrabajoForm()
    direccion = Direccion.objects.filter(Persona = usuario_solicitud).order_by('-Principal')
    data['direcciones'] = direccion

    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    data['regiones'] = regiones
    data['comunas'] = comunas

    trabajos = Trabajo.objects.all()
    validar_trabajos(trabajos)

    return render(request, 'publicar_trabajo.html', data)

@login_required(login_url='/auth/login')
def guardar_trabajo(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    print("Guardar trabajo")
    print(pk_user)
    print(usuario.pk)
    if (request.method == 'GET'):
        print("get")

    if (request.method == 'POST'):
        print("hola")

        print("Guardar trabajo")
        print(pk_user)
        print(usuario.pk)

        #Obtengo los atributos
        print("POSSST BEIBE")
        print(request.POST)
        print("")
        print(request.FILES)
        nombre = request.POST["nombre"]
        detalle = request.POST["detalle"]
        monto = request.POST["monto"]
        area = request.POST["id_Area"]
        r_etario = request.POST["tiempo_aproximado"]
        direccion = request.POST.get('direccion', False)


        if(direccion):
            direccion_object = Direccion.objects.get(pk=direccion)
            print("si aqui")
        else:
            print("nop, aqui")
            comuna = request.POST["comuna"]
            calle = request.POST["calle"]
            num_calle = request.POST["numero_calle"]
            direccion_object = Direccion()
            direccion_object.Persona = usuario
            direccion_object.Comuna = Comuna.objects.get(pk = comuna)
            direccion_object.Numero_de_calle = num_calle

            direccion_object.Calle = calle
            direccion_object.Principal = 0
            direccion_object.save()
            print(direccion_object)
        fecha = request.POST["fecha"]
        # hora = request.POST["hora"]
        personas_requeridas = request.POST['personas_requeridas']
        imagen = request.FILES["ImagenTrabajo"]


        #handle_uploaded_file(imagen)
#
        area_object = Areas.objects.get(pk=area)

        print("creando trabajo...")
        trabajo = Trabajo()
        print("pk usuario: "+str(usuario.pk))
        #FORMATO FECHA
        # s = '2004/03/31'
        fecha_vencimiento = request.POST.get('fecha_vencimiento', False)
        if(fecha_vencimiento):

            pass
        else:
            aux = datetime.strptime(fecha, "%Y-%m-%dT%H:%M")
            fecha_vencimiento = aux + timedelta(days=2)
            datetime.strftime(fecha_vencimiento, "%Y/%m/%d")
            print(fecha_vencimiento)
        #
        trabajo.Usuario = usuario
        print("trabajo usuario: "+str(trabajo.Usuario.pk))
        # trabajo.Fecha_vencimiento = fecha_vencimiento
        trabajo.Fecha_vencimiento = fecha_vencimiento

        print(trabajo.Fecha_vencimiento )
        print(trabajo.Fecha_vencimiento )
        trabajo.Nombre = nombre
        trabajo.Detalle = detalle
        trabajo.Monto_pago = monto
        trabajo.Area = area_object
        trabajo.rango_etario = r_etario
        trabajo.Direccion = direccion_object
        trabajo.Fecha = fecha
        print(type(fecha))
        print(type(trabajo.Fecha))


        # trabajo.Hora = hora
        trabajo.Imagen = imagen
        trabajo.Personas_requeridas = personas_requeridas
        trabajo.Vacantes = personas_requeridas
        trabajo.save()
        print(trabajo)

        #crear historial
        historial = Historial_trabajo()
        historial.Persona = usuario
        historial.Trabajo = trabajo
        historial.save()
        print(historial)
    return redirect('visualizar_perfil', request.user.pk)
    # return render(request, 'publicar_trabajo.html', data)
