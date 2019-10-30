
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Publicar_trabajo.models import *

# Create your views here.
@login_required(login_url='/auth/login')
def index_admin(request):

    print("hola")
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud


    return render(request, 'index_admin.html', data)

@login_required(login_url='/auth/login')
def adm_usuarios(request):

    print("hola")
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    usuarios = Persona.objects.all()
    data['usuarios'] = usuarios


    return render(request, 'adm_usuarios.html', data)
@login_required(login_url='/auth/login')
def adm_pegas(request):

    print("hola")
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    pegas = Trabajo.objects.all()
    pegas2 = Trabajo.objects.order_by('-Fecha')

    print(pegas)
    print(pegas2)
    # print(pegas)
    data['pegas'] = pegas2


    return render(request, 'adm_pegas.html', data)

@login_required(login_url='/auth/login')
def visualizar_perfil_adm(request,pk_user):
    data = {}

    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario
    # print(usuario.pk)
    print(request.user.pk)
    print(pk_user)
    return render(request, 'visualizar_perfil_adm.html', data)

@login_required(login_url='/auth/login')
def visualizar_pega_adm(request,pk_pega):
    data = {}
    pega = Trabajo.objects.get(pk = pk_pega)
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    usuario = Persona.objects.get(Usuario=pega.Usuario.Usuario.pk)
    data['usuario'] = usuario
    data['pega'] = pega

    print(usuario.Nombre)
    print(usuario.privilegios)

    return render(request, 'visualizar_pega_adm.html', data)
