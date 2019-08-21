from django.shortcuts import render
from Registro_fullpega.models import *
from Registro_fullpega.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    a = 'jj'
    data = {a: 'holiwis'}

    return render(request, 'index_super_user.html', data)

# @login_required(login_url='/auth/login')
def pagina_principal(request):
    # a = 'jj'
    data = {}

    return render(request, 'pagina_principal.html', data)


#def Registro_form(request):
#    data = {}
#    return render(request, 'pages_register.html', data)



# def Registro_form(request):
#     data = {}
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ClienteForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             #return HttpResponseRedirect('/thanks/')
#             print("hola estas en registro form")
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ClienteForm()
#
#     return render(request, 'pages_register.html', {'form': form})
@login_required(login_url='/auth/login')
def visualizar_perfil(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario

    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'visualizar_perfil.html', data)

@login_required(login_url='/auth/login')
def visualizar_privilegios(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario

    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'visualizar_privilegios.html', data)

@login_required(login_url='/auth/login')
def buscar_trabajo(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario

    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'buscar_trabajo.html', data)

@login_required(login_url='/auth/login')
def h_trabajos_realizados(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario

    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'h_trabajos_realizados.html', data)

@login_required(login_url='/auth/login')
def h_trabajos_publicados(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario

    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'h_trabajos_publicados.html', data)


def Registro_form(request):

    template_name = 'pages_register.html'
    data = {}
    data['form'] = UserForm()
    data['form2'] = ClienteForm()
    if request.method == "POST":
        data['form'] = UserForm(request.POST, request.FILES)

        if (data['form'].is_valid()):
            print("DATA 1 VALID")
            if (request.POST["password1"] == request.POST["password2"]):
                if (len(request.POST["password1"]) >= 4):
                    user = User.objects.create_user(username=request.POST["username"],
                                                    password=request.POST["password1"])
                    user.save()
                    datos = ClienteForm(request.POST, request.FILES)
                    if (datos.is_valid()):
                        print(user)
                        datos = datos.save(commit=False)
                        #rescatando datos de cliente
                        usuario = User.objects.get(pk=user.pk)
                        datos.usuario = usuario
                        datos.privilegio = 'Sp'
                        datos.save()
                    else:
                        print("else de data 2")

                    return redirect('index')
                else:
                    print("else 1")
                    messages.warning(
                        request,
                        'El largo de la contraseña debe ser mayor a 8'
                    )
            else:
                print("else 2")
                messages.error(
                    request,
                    'Las contraseñas no coinsiden'
                )

        else:
            print("else 3")
            data['form'] = UserForm()
            messages.error(
                request,
                'La Contraseña es Similar al Nombre de Usuario'
            )
    return render(request, template_name, data)
