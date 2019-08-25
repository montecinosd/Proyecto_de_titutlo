from django.shortcuts import render
# from Registro_fullpega.models import *
# from Registro_fullpega.forms import *
from Publicar_trabajo.models import *
from Publicar_trabajo.forms import *

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

# Create your views here.
@login_required(login_url='/auth/login')
def publicar_trabajo(request,pk_user):
    data = {}
    areas = Areas.objects.all()
    usuario = Persona.objects.filter(Usuario=pk_user)
    print(usuario)
    data['usuario'] = usuario
    data['areas'] = areas
    data['form'] = TrabajoForm()


    return render(request, 'publicar_trabajo.html', data)

@login_required(login_url='/auth/login')
def guardar_trabajo(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    print(usuario)
    # data['usuario'] = usuario
    # data['areas'] = areas
    # data['form'] = TrabajoForm()

    if request.method == 'GET':
        print("get")
    if request.method == 'POST':
        #Obtengo los atributos
        print("POSSST BEIBE")
        print(request.POST)
        print(request.FILES)
        nombre = request.POST["nombre"]
        detalle = request.POST["detalle"]
        monto = request.POST["monto"]
        area = request.POST["id_Area"]
        r_etario = request.POST["r_etario"]
        direccion = request.POST["direccion"]
        fecha = request.POST["fecha"]
        hora = request.POST["hora"]
        imagen = request.FILES["imagen"]
        print(type(imagen))
        # handle_uploaded_file(imagen)
#
        area_object = Areas.objects.get(pk=area)
        direccion_object = Direccion.objects.get(pk=direccion)

        trabajo = Trabajo()
        trabajo.Usuario = usuario
        trabajo.Nombre = nombre
        trabajo.Detalle = detalle
        trabajo.Monto_pago = monto
        trabajo.Area = area_object
        trabajo.rango_etario = r_etario
        trabajo.Direccion = direccion_object
        trabajo.Fecha = fecha
        trabajo.Hora = hora
        trabajo.Imagen = imagen
        trabajo.save()


    return redirect('visualizar_perfil', request.user.pk)
    # return render(request, 'publicar_trabajo.html', data)
