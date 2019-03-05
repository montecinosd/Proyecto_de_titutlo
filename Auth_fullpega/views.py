from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def auth_login(request):
    template_name = 'pages_login.html'
    # template_name = 'login.html'
    data = {}

    logout(request)
    username = password = ''
    print("ASDS")
    print(request.POST)
    if request.POST:
        print("POSTXD")
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Usuario o contraseña no validos")
                messages.warning(
                    request,
                    'Usuario o contraseña incorrectos'
                )
        else:
            print("Usuario incorrecto")
            messages.error(
                request,
                'Usuario o contraseña incorrectos'
            )
    return render(request, template_name, data)


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
