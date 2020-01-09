from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_protect

import random
import string
from Correos.views import *

def generar_Contrasenha(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@csrf_protect
def auth_login(request):
    template_name = 'pages_login.html'
    # template_name = 'login.html'
    data = {}

    logout(request)
    username = password = ''
    # print("ASDS")
    # print(request.POST)
    if request.POST:
        print("POSTXD")
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            # if user.is_active:
            #     login(request, user)
            #     return HttpResponseRedirect(reverse('index'))
            if user and user.is_staff is False:
                login(request, user)
                # return HttpResponseRedirect(reverse('index'))
                return redirect('visualizar_perfil',request.user.pk)
            elif user and user.is_staff is True:
                login(request, user)
                return redirect('index_admin')

            else:
                print("Usuario o contraseña no validos")
                # messages.warning(
                #     request,
                #     'Usuario o contraseña incorrectos'
                # )
        else:
            print("Usuario incorrecto")
            # messages.error(
            #     request,
            #     'Usuario o contraseña incorrectos'
            # )
    return render(request, template_name, data)

@csrf_protect
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@csrf_protect
def restablecer_contrasenha(request):
    data={}
    if(request.POST):
        print(request)
        print("post")
        contrasenha = generar_Contrasenha(10)
        print(contrasenha)
        print(request.POST['mail'])
        user = User.objects.get(username = 'c.gonzalez@gmail.com')
        user.set_password(contrasenha)
        enviar_emails("Cambio de contraseña FullPega","Se ha cambiado su contraseña, su contraseña provisional es "+contrasenha+". Le recordamos que luego puede actualizar en sus configuraciones. <br> FullPega nunca te pedirá datos personales ni contraseñas. <br> Equipo FullPega.-",["danielmontecinoszambra@gmail.com"])
        user.save()
        return render(request,'restablecer_contrasenha_mensaje.html',data)
        # print(user.password)

    return render(request,'restablecer_contrasenha.html',data)
