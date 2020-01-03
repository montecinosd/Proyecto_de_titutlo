from django.shortcuts import render
from Publicar_trabajo.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
import datetime



@login_required(login_url='/auth/login')
def config_perfil(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=request.user.pk)
    data['usuario'] = usuario
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    data['regiones'] = regiones
    data['comunas'] = comunas

    data['areas'] = Areas.objects.all()
    data['preferencias'] = Preferencias.objects.get(Usuario = usuario)
    Direcciones = Direccion.objects.filter(Persona = usuario)
    data['direcciones'] = Direcciones
    print(Direcciones)
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud


    return render(request, 'config_perfil.html', data)

@login_required(login_url='/auth/login')
def config_direccion(request, pk_direccion):
    data = {}
    usuario = Persona.objects.get(Usuario=request.user.pk)
    print(request)
    if(pk_direccion==0):
        pass
    else:
        direccion = Direccion.objects.get(pk = pk_direccion)
        data['direccion'] = direccion
    data['usuario'] = usuario
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    direcciones = Direccion.objects.filter(Persona = usuario)
    data['regiones'] = regiones
    data['comunas'] = comunas

    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    return render(request, 'config_direccion.html', data)
    # return redirect('config_perfil', request.user.pk)
@login_required(login_url='/auth/login')
def config_direccion_actualizar(request, pk_direccion):
    data = {}
    usuario = Persona.objects.get(Usuario=request.user.pk)
    calle = request.POST['calle']
    n_calle = request.POST['numero_calle']
    region = request.POST['region']
    comuna = request.POST['comuna']
    print(request.POST)
    direcciones = Direccion.objects.filter(Persona = usuario)
    print(direcciones)
    print(request)
    if(pk_direccion ==0):
        direccion = Direccion()
        direccion.Persona = usuario
        pass
    else:
        direccion = Direccion.objects.get(pk=pk_direccion)
        print(direccion)

    if( 'direccion_principal' in request.POST):
        for i in direcciones:
            i.apagar_principal()
            i.save()
        direccion.establecer_principal()
    else:
        direccion.apagar_principal()

    direccion.Numero_de_calle = n_calle
    direccion.Calle = calle
    print(comuna)
    comuna1 = Comuna.objects.get(pk = comuna)
    direccion.Comuna = comuna1
    region1 = Region.objects.get(pk = region)
    direccion.Comuna.region = region1
    direccion.save()

    return redirect('config_perfil', request.user.pk)

@login_required(login_url='/auth/login')
def guardar_config_datos(request):
    data = {}
    usuario = Persona.objects.get(Usuario=request.user.pk)
    print(request.POST)
    print(request.FILES)
    print(usuario.Imagen)

    if(request.POST['imagenRegistro2'] != ''):
        print("hay foto")
        imagen = request.FILES['imagenRegistro']
        usuario.Imagen = imagen

        pass
    else:
        print("no hay foto")
        pass
    telefono = request.POST['telefono']
    correo = request.POST['mail']
    usuario.Telefono_C = telefono
    usuario.Correo = correo
    usuario.save()

    return redirect('config_perfil', request.user.pk)

@login_required(login_url='/auth/login')
def guardar_config_perfil_preferencias(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    print(usuario)

    if request.method == 'GET':
        print("get")
    if request.method == 'POST':
        valores = {}
        if (request.POST.get("comuna")):
            valores['Comuna'] = Comuna.objects.get(pk = request.POST['comuna'])
        if (request.POST.get("m_minimo")):
            valores['M_minimo'] = request.POST['m_minimo']
        if (request.POST.get("m_maximo")):
            valores['M_maximo'] = request.POST['m_maximo']
        if (request.POST.get("area")):
            valores['Area'] = Areas.objects.get(pk = request.POST['area'])
        #crea o actualiza la preferencia
        preferencia, preferencia_creada = Preferencias.objects.update_or_create(Usuario = usuario, defaults = valores)

        print(request.POST)
        if (preferencia_creada):
            print("creada")
        else:
            print("ya tenia")
        print( preferencia)
        print( preferencia_creada)
        # m_minimo = request.POST.get("")
        # Preferencias.objects.create(usuario=usuario, m_minimo = ,m_maximo = ,direccion = )
        #                       region=self)
    # return render(request, 'visualizar_perfil.html', data)
    return redirect('config_perfil', request.user.pk)

def enviar_correo_inactivos():

    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)
    last_month = today - datetime.timedelta(days=31)
    # start_date, end_date
    usuarios_inactivos = Persona.objects.filter(Usuario__last_login__range=(last_month, last_week))

    # for i in usuarios_inactivos:

    print(usuarios_inactivos)
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
