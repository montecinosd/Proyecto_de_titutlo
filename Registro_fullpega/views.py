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


# Create your views here.
@login_required(login_url='/auth/auth_login')
def index(request):
    a = 'jj'
    data = {a: 'holiwis'}

    return render(request, 'index_super_user.html', data)


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
                    data['form2'] = ClienteForm(request.POST, request.FILES)
                    print(data['form2'])
                    if (data['form2'].is_valid()):
                        print("DATA 2VALID")
                        data['form2'].save(commit=False)
                        #rescatando datos de cliente
                        cliente = Cliente()
                        cliente.usuario = user
                        cliente.privilegio = 'Sp'
                       # fields = ['Nombre', 'Fecha_nacimiento', 'Email', 'Direccion', 'rut', 'dv']

                       # cliente.Email = request.POST["Email"]
                        cliente.save()
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
