from django.shortcuts import render
from Publicar_trabajo.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.



@login_required(login_url='/auth/login')
def config_perfil(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario

    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud


    return render(request, 'config_perfil.html', data)

    # return redirect('config_perfil', request.user.pk)

@login_required(login_url='/auth/login')
def guardar_config_perfil_redes(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    print(usuario)

    if request.method == 'GET':
        print("get")
    if request.method == 'POST':
        #Obtengo los atributos
        print("POSSST BEIBE")
        print(request.POST)
        print("request files")
        # print(request.FILES)
        print("request files fin ")

        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']
        instagram = request.POST['instagram']

        usuario.Facebook = facebook
        usuario.Twitter = twitter
        usuario.Linkedin = linkedin
        usuario.Instagram = instagram

        usuario.save()

    # return render(request, 'visualizar_perfil.html', data)
    return redirect('config_perfil', request.user.pk)
