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
from Publicar_trabajo.models import *

# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud



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

    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario
    # print(usuario.pk)
    print(request.user.pk)
    print(pk_user)
    if (request.user.pk == pk_user):
        return render(request, 'visualizar_perfil.html', data)
    else:
        return render(request, 'visualizar_perfil_noprivilegios.html', data)
    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
def visualizar_perfil_detalle_pega(request,pk_pega):
    data = {}
    pega = Trabajo.objects.get(pk = pk_pega)
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    usuario = Persona.objects.get(Usuario=pega.Usuario.Usuario.pk)
    data['usuario'] = usuario
    data['pega'] = pega
    # print(usuario.pk)
    # print(request.user.pk)
    # print(pk_user)
    print(usuario.Nombre)
    print(usuario.privilegios)
    if (usuario_solicitud.privilegios == 2):
        print("privilegios")
        return render(request, 'visualizar_perfil_privilegios.html', data)
    else:
        print("no privilegios")
        return render(request, 'visualizar_perfil_noprivilegios.html', data)
    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
def visualizar_perfil_postulante(request,pk_postulante):
    data = {}


    postulante = Postulantes.objects.get( pk = pk_postulante)
    # pega = Trabajo.objects.get(pk = pk_user)
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    #se rescata pk de usuario
    usuario = Persona.objects.get(Usuario=postulante.Postulante.pk)
    pega = Trabajo.objects.get(pk=postulante.Trabajo.pk)
    data['usuario'] = usuario
    data['pega'] = pega
    data['postulante'] = postulante
    # print(usuario.pk)
    # print(request.user.pk)
    # print(pk_user)
    print(usuario.Nombre)
    print(usuario.privilegios)
    if (usuario_solicitud.privilegios == 3):
        print("visualizar postulante privilegios")
        return render(request, 'visualizar_perfil_postulante_privilegio.html', data)
    else:
        print("visualizar postulante no privilegios")
        return render(request, 'visualizar_perfil_postulante_noprivilegio.html', data)

    # return render(request, 'visualizar_pefrfil_postulante_privilegio.html', data)

@login_required(login_url='/auth/login')
def postulante_acordado(request,pk_postulante):
    data = {}
    print("guardando trabajo acordado...")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

#se crea el objeto del acuerdo de trabajo, con lo cual se realizará
    postulante_acordado = Postulantes.objects.get(pk = pk_postulante)
    trabajo_acordado = Trabajo_acordado()
    trabajo_acordado.postulante_acordado = postulante_acordado

    trabajo_acordado.save()

@login_required(login_url='/auth/login')
def cerrar_trabajo_publicado(request,pk_postulante):
    data = {}
    print(request.POST)
#     usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
#     data['usuario_solicitud'] = usuario_solicitud
#
# #se crea el objeto del acuerdo de trabajo, con lo cual se realizará
#     postulante_acordado = Postulantes.objects.get(pk = pk_postulante)
#     trabajo_acordado = Trabajo_acordado()
#     trabajo_acordado.postulante_acordado = postulante_acordado
#
#     trabajo_acordado.save()

    # usuario = Persona.objects.get(Usuario=pk_user)
    # trabajo = Trabajo.objects.get(pk=pk_pega)
    #
    # # guardando el postulante
    # postulantes = Postulantes()
    # postulantes.Trabajo= trabajo
    # postulantes.Postulante = usuario_solicitud
    # postulantes.save()


@login_required(login_url='/auth/login')
def postular_inicial(request,pk_pega):
    data = {}
    print("postulando...")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    # usuario = Persona.objects.get(Usuario=pk_user)
    trabajo = Trabajo.objects.get(pk=pk_pega)

    # guardando el postulante
    postulantes = Postulantes()
    postulantes.Trabajo= trabajo
    postulantes.Postulante = usuario_solicitud
    postulantes.save()

@login_required(login_url='/auth/login')
def visualizar_postulantes_a_trabajos(request, pk_user):
    data = {}
    print("postulando...")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    # usuario = Persona.objects.get(Usuario=pk_user)
    trabajos = Trabajo.objects.filter(Usuario = usuario_solicitud.pk).exclude(Activo=0)
    data['trabajos'] = trabajos
    data['postulantes'] = Postulantes.objects.all()
    # for i in trabajos:
    #     postulantes = Postulantes.objects.filter(Trabajo = i.pk)
    #     for z in postulantes:
    #         print(type(z))
    #     data["postulantes"]=postulantes
    print(type(data["trabajos"]))


    print(data)
    # data['trabajos'] = trabajos
    print("trabajos: "+str(data['trabajos']))


    return render(request, 'visualizar_postulantes.html', data)

@login_required(login_url='/auth/login')
def visualizar_trabajo_activo(request, pk_user):
    data = {}
    print("...")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    # a = Trabajo_acordado()
    # a.postulante_acordado.Trabajo.Usuario.Usuario.

    trabajos_acordados = Trabajo_acordado.objects.all().filter(postulante_acordado__Trabajo__Usuario__Usuario = usuario_solicitud)
    # trabajos_acordados = Trabajo_acordado.objects.all().exclude(postulante_acordado__Trabajo__Usuario__Usuario = usuario_solicitud)
    print(trabajos_acordados)
    data['trabajos_acordados'] = trabajos_acordados
    # trabajos_acordados = Trabajo_acordado()
    # trabajos_acordados.
    print(trabajos_acordados)


    return render(request, 'visualizar_trabajo_activo.html', data)

@login_required(login_url='/auth/login')
def visualizar_privilegios(request,pk_user):
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario

    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'visualizar_privilegios.html', data)

@login_required(login_url='/auth/login')
def buscar_trabajo(request,pk_user):

    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    usuario = Persona.objects.get(Usuario=pk_user)

    #excluir mismo usuario
    trabajos = Trabajo.objects.filter(Activo = 1).exclude(Usuario__Usuario= usuario)
    data['trabajos'] = trabajos
    data['usuario'] = usuario
    print(data)

    print(data)
    return render(request, 'buscar_trabajo.html', data)

@login_required(login_url='/auth/login')
def h_trabajos_realizados(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'h_trabajos_realizados.html', data)

@login_required(login_url='/auth/login')
def h_trabajos_publicados(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    historico = Historial_trabajo.objects.filter(Persona = usuario)
    data["historial_trabajos_publicados"] = historico
    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'h_trabajos_publicados.html', data)


def Guardar_Registro_form(request):
    if request.method =='GET':
        print("GET:................")
    if request.method == "POST":
        print("POSTTTTTTTTTTTTTTTTT")
        print(request.POST)
        print(request.FILES)
        comuna = request.POST['comuna']
        apellidos = request.POST['apellidos']
        imagen = request.FILES['imagenRegistro']
        f_nacimiento = request.POST['f_nacimiento']
        pais= request.POST['pais']
        mail = request.POST['email']
        numero_calle = request.POST['numero_calle']
        contrasena2= request.POST['confirmPassword']
        contrasena1 = request.POST['password']
        rut = request.POST['rut']
        region = request.POST['region']
        telefono= request.POST['telefono']
        nombres = request.POST['nombres']
        ciudad = request.POST['ciudad']
        calle = request.POST['calle']

        if (contrasena1 == contrasena2):
            if (len(contrasena1) >= 4):
                user = User.objects.create_user(username=mail,
                                                password=contrasena1)
                user.save()

                persona = Persona()

                persona.Usuario = user
                persona.Imagen = imagen
                persona.Telefono_C = telefono
                persona.Rut = rut
                persona.Correo = mail
                persona.Nombre = nombres
                persona.Fecha_nacimiento = f_nacimiento

                #direccion
                direccion = Direccion()
                direccion.Calle = calle
                direccion.Ciudad = ciudad
                direccion.Comuna = comuna
                direccion.Numero_de_calle = numero_calle
                direccion.Pais = pais
                direccion.save()

                persona.Direccion = direccion
                persona.save()




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
                'Las contraseñas no coinciden'
            )

    return redirect('auth_login')

def Registro_form(request):

    template_name = 'pages_register.html'
    data = {}
    # data['form'] = UserForm()
    # data['form2'] = ClienteForm()

    print("AQUI XD")
    if request.method =='GET':
        print("GET:................")
    if request.method == "POST":
        print("POSTTTTTTTTTTTTTTTTT")
        print(request.POST)
        print("hola")

        # data['form'] = UserForm(request.POST, request.FILES)
        # if (request.POST["password1"] == request.POST["password2"]):
        #     if (len(request.POST["password1"]) >= 4):
        #         user = User.objects.create_user(username=request.POST["email"],
        #                                         password=request.POST["password1"])
                # email = request.POST['email']
                # user.save()
                # datos = ClienteForm(request.POST, request.FILES)

                # persona = Persona()
                # persona.Nombre = request.POST['nombres']
                # persona.Correo = request.POST['email']
                # persona.Rut = request.POST['rut']
                # persona.Telefono_C = request.POST['telefono']
                # persona = request.POST['']
                # persona = request.POST['']

            # else:
            #     print("else 1")
            #     messages.warning(
            #         request,
            #         'El largo de la contraseña debe ser mayor a 8'
            #     )

        # else:
        #     print("else 2")
        #     messages.error(
        #         request,
        #         'Las contraseñas no coinsiden'
        #     )

    return render(request, template_name, data)

            # if (data['form'].is_valid()):
        #     print("DATA 1 VALID")
        #     if (request.POST["password1"] == request.POST["password2"]):
        #         if (len(request.POST["password1"]) >= 4):
        #             user = User.objects.create_user(username=request.POST["username"],
        #                                             password=request.POST["password1"])
        #             user.save()
        #             datos = ClienteForm(request.POST, request.FILES)
        #             if (datos.is_valid()):
        #                 print(user)
        #                 datos = datos.save(commit=False)
        #                 #rescatando datos de cliente
        #                 usuario = User.objects.get(pk=user.pk)
        #                 datos.usuario = usuario
        #                 datos.privilegio = 'Sp'
        #                 datos.save()
        #             else:
        #                 print("else de data 2")
        #
        #             return redirect('index')
        #         else:
        #             print("else 1")
        #             messages.warning(
        #                 request,
        #                 'El largo de la contraseña debe ser mayor a 8'
        #             )

        # else:
        #     print("else 3")
        #     data['form'] = UserForm()
        #     messages.error(
        #         request,
        #         'La Contraseña es Similar al Nombre de Usuario'
        #     )

@login_required(login_url='/auth/login')
def config_perfil(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario


    #
    # if request.method == 'GET':
    #     print("get")
    # if request.method == 'POST':
    #     #Obtengo los atributos
    #     print("POSSST BEIBE")
    #     print(request.POST)
    #     print(request.FILES)
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
