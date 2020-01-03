from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import operator
from Publicar_trabajo.views import validar_trabajos
from Publicar_trabajo.models import *
from sensibilidad_watson.watson import *
from django.db.models import CharField, Value
from Correos.views import *
from Configuracion_perfil.views import *
# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    data = {}
    # respueta_watson = getSentimentValue("Muy mal no pago a tiempo  -    ")
    # print("respuesta watson: "+str(respueta_watson))
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    # notificaciones = Notificaciones.objects.filter(usuario = usuario_solicitud)
    # print(notificaciones)
    # data['notificaciones'] = notificaciones

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
    postulante_acordado = Postulantes.objects.get(pk = pk_postulante) # esta pk es la del postulante, por lo que está bien. no es la pk de la persona. siempre rescata la postulacion en sí.
    postulante_acordado.Estado = 1
    postulante_acordado.save()
    aux_trabajo = Trabajo.objects.get(pk = postulante_acordado.Trabajo.pk)
    aux_trabajo.Vacantes = aux_trabajo.Vacantes - 1
    aux_trabajo.save()
    # postulante_acordado.Trabajo.Vacantes = postulante_acordado.Trabajo.Vacantes - 1
    # postulante_acordado.save()

    trabajo_acordado = Trabajo_acordado()
    trabajo_acordado.postulante_acordado = postulante_acordado

    trabajo_acordado.save()
    #notificacion a postulante acordado
    notificacion = Notificaciones()
    notificacion.usuario = postulante_acordado.Postulante
    notificacion.Tipo = 2 # notificacion a postulante acordado
    notificacion.Trabajo_acordado = trabajo_acordado
    notificacion.save()
    return redirect('visualizar_trabajo_activo', request.user.pk)


@login_required(login_url='/auth/login')
def cerrar_trabajo_publicado(request,pk_trabajo):
    data = {}
    print(request.POST)
    print(pk_trabajo)
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    trabajo = Trabajo.objects.get(pk = pk_trabajo)
    trabajos_acordados = Trabajo_acordado.objects.filter(postulante_acordado__Trabajo = trabajo)
    print(trabajo.Nombre)
    print(trabajos_acordados)

    # CERRAR TRABAJO
    trabajo.Activo = 0
    trabajo.save()

    # HISTORICO TRABAJO REALIZADO
    for i in trabajos_acordados:
        # print(i.postulante_acordado.Postulante)
        historico_realizado = Historial_trabajo()
        historico_realizado.Trabajo = trabajo
        historico_realizado.Persona = i.postulante_acordado.Postulante
        historico_realizado.tipo = 2 # 2 es que lo realizo
        historico_realizado.save()

    # CALIFICACION - se deja la calificacion lista para luego solo "rellenarla" en template de puntuaciones pendientes
    for i in trabajos_acordados:
        calificacion = Calificaciones()
        calificacion.Pega_calificada = trabajo
        calificacion.usuario_calificador = usuario_solicitud
        calificacion.usuario = i.postulante_acordado.Postulante
        calificacion.save()
        #calificacion para el requirente
        calificacion2 = Calificaciones()
        calificacion2.Pega_calificada = trabajo
        calificacion2.usuario_calificador = i.postulante_acordado.Postulante
        calificacion2.usuario = usuario_solicitud
        calificacion2.save()


    # NOTIFICACION
    for i in trabajos_acordados:
        notificacion = Notificaciones()
        notificacion.Trabajo_acordado = i
        notificacion.usuario = i.postulante_acordado.Postulante
        notificacion.save()

    '''

    ## INFORMACION DE LA PAGINA
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    trabajos_acordados = Trabajo_acordado.objects.all().filter(postulante_acordado__Trabajo__Usuario__Usuario = usuario_solicitud).exclude(postulante_acordado__Trabajo__Activo = 0)
    print(trabajos_acordados)

    data['trabajos_acordados'] = trabajos_acordados
    ##FIN INFO PAGINA

    # CERRAR TRABAJO
    trabajo_acordado = Trabajo_acordado.objects.get(pk = pk_trabajo_acordado)
    print(trabajo_acordado.postulante_acordado.Trabajo.Nombre)

    trabajo_acordado.postulante_acordado.Trabajo.Activo = 0
    trabajo_acordado.postulante_acordado.Trabajo.save()
    #FIN CERRAR TRABAJO

    #CALIFICACION
    calificacion = Calificaciones()

    #usuario_solicitud -> usuario_calificador
    usuario_calificado = Persona.objects.get(pk=trabajo_acordado.postulante_acordado.Postulante.pk)
    #trabajo_acordado -> pega acordado
    estrellas = request.POST['stars']
    comentarios = request.POST['comentario']
    print(estrellas)
    print(comentarios)
    #
    calificacion.usuario_calificador = usuario_solicitud
    calificacion.usuario = usuario_calificado
    calificacion.Estrellas = estrellas
    calificacion.Comentarios = comentarios
    calificacion.Pega_calificada = trabajo_acordado.postulante_acordado.Trabajo
    calificacion.save()
    #FIN CALIFICACION

    #HISTORICO TRABAJO REALIZADO
    historico_realizado = Historial_trabajo()
    historico_realizado.Trabajo = trabajo_acordado.postulante_acordado.Trabajo
    historico_realizado.Persona = usuario_calificado
    historico_realizado.tipo = 2
    historico_realizado.save()
    #FIN TRABAJO REALIZADO

    #NOTIFICACION
    notificacion = Notificaciones()
    notificacion.Trabajo_acordado = trabajo_acordado
    notificacion.usuario = usuario_calificado
    notificacion.save()
'''
    return render(request, 'visualizar_trabajo_activo.html', data)
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
def calificar_oferente(request,pk_notificacion):
    #ES EL QUE HIZO EL TRABAJO
    print("ENTRANDO...")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)

    notificacion = Notificaciones.objects.get(pk = pk_notificacion)

    # CALIFICACION
    notificacion.Activo = 0
    notificacion.save()
    calificacion = Calificaciones()

    # usuario_solicitud -> usuario_calificador
    usuario_calificado = notificacion.Trabajo_acordado.postulante_acordado.Trabajo.Usuario
    # trabajo_acordado -> pega acordado
    print(request.POST)
    estrellas = request.POST.get('stars')
    comentarios = request.POST.get('comentario')
    print(estrellas)
    print(comentarios)
    #
    calificacion.usuario_calificador = usuario_solicitud
    calificacion.usuario = usuario_calificado
    calificacion.Estrellas = estrellas
    calificacion.Comentarios = comentarios
    calificacion.Pega_calificada = notificacion.Trabajo_acordado.postulante_acordado.Trabajo
    calificacion.save()
    # FIN CALIFICACION

    # return HttpResponseRedirect(request.path_info)
    return render(request, 'index_super_user.html')



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
    #notificacion de que postulo alguien
    notificacion = Notificaciones()
    notificacion.usuario =trabajo.Usuario
    notificacion.Tipo = 3
    notificacion.Trabajo = trabajo
    notificacion.save()

    return redirect('buscar_trabajo', pk_pega)

@login_required(login_url='/auth/login')
def visualizar_postulantes_a_trabajos(request, pk_user):
    data = {}
    print("postulando...")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    # usuario = Persona.objects.get(Usuario=pk_user)
    trabajos = Trabajo.objects.filter(Usuario = usuario_solicitud.pk).exclude(Activo=0)
    validar_trabajos(trabajos)
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
def visualizar_postulantes_detalle(request, pk_pega):
    data = {}
    print("postulando...")
    trabajo = Trabajo.objects.get( pk = pk_pega)

    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    # usuario = Persona.objects.get(Usuario=pk_user)
    trabajos = Trabajo.objects.filter(Usuario = usuario_solicitud.pk).exclude(Activo=0)
    # validar_trabajos(trabajos)
    data['trabajo'] = trabajo
    data['trabajos'] = trabajos
    data['postulantes'] = Postulantes.objects.filter(Trabajo = trabajo)
    print(type(data["trabajos"]))


    print(data)
    # data['trabajos'] = trabajos
    print("trabajos: "+str(data['trabajos']))


    return render(request, 'visualizar_postulantes_detalle.html', data)
@login_required(login_url='/auth/login')
def visualizar_postulantes_detalle_watson(request, pk_pega):
    data = {}
    print("postulando...")
    trabajo = Trabajo.objects.get( pk = pk_pega)

    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    # usuario = Persona.objects.get(Usuario=pk_user)
    trabajos = Trabajo.objects.filter(Usuario = usuario_solicitud.pk).exclude(Activo=0)
    data['trabajo'] = trabajo
    data['trabajos'] = trabajos
    postulantes = Postulantes.objects.filter(Trabajo=trabajo)
    data['postulantes'] = postulantes
    print(type(data["trabajos"]))
    list = [1,2,5,8,3]
    list.sort()
    print("HOLA"+str(list))

    aux_Dic = {}
    Dic = {}
    for i in postulantes:
        ponderacion = 0
        print(i.Postulante.Direccion.Comuna)
        print('1-',i.Postulante.Nombre,' ',ponderacion)
        if(trabajo.Direccion.Comuna == i.Postulante.Direccion.Comuna):
            print("es la misma direccion!!!")
            ponderacion +=1
        # print('1-',i.Postulante.Nombre,' ',ponderacion)

        aux= 0.2*float(i.Postulante.Estrellas)
        print('2-',i.Postulante.Nombre,' ',ponderacion)

        print(aux)
        ponderacion += aux
        print('3-',i.Postulante.Nombre,' ',ponderacion)

        ponderacion += i.Postulante.Puntaje_watson
        print('4-',i.pk,i.Postulante.Nombre,' ',ponderacion)

        Dic[i]=ponderacion

        print(i.Postulante.Nombre +'tiene de ponderacion '+str(ponderacion))
    # miDic = {"a": [2,10], "b": [3,10], "d": [1,10], "c": [1,10]}
    # resultado = sorted(miDic.items(), key=operator.itemgetter(1))
    #ordena de menor a mayor y luego se hace un reverse para que queden los puntajes mas altos
    resultado2 = sorted(Dic.items(), key=operator.itemgetter(1))
    resultado2 =resultado2[::-1]
    # print(resultado)
    print(resultado2)
    for i in resultado2:
        print(i[0].Postulante.Nombre)

    # data['trabajos'] = trabajos
    print("trabajos: "+str(data['trabajos']))
    data['postulantes2'] = resultado2
    data['ejemplo'] = [5,4,3,2,42]

    return render(request, 'visualizar_postulantes_detalle_watson.html', data)
@login_required(login_url='/auth/login')
def visualizar_trabajo_activo(request, pk_user):
    data = {}
    print("...")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    # a = Trabajo_acordado()
    # a.postulante_acordado.Trabajo.Usuario.Usuario.

    trabajos_acordados = Trabajo_acordado.objects.all().filter(postulante_acordado__Trabajo__Usuario__Usuario = usuario_solicitud).exclude(postulante_acordado__Trabajo__Activo = 0)
    # trabajos_acordados = Trabajo_acordado.objects.all().exclude(postulante_acordado__Trabajo__Usuario__Usuario = usuario_solicitud)
    print(trabajos_acordados)
    data['trabajos_acordados'] = trabajos_acordados

    # RESCATO LOS TRABAJOS (PKS) PARA ARMAR EL TEMPLATE CON IDS, el aux es para sacar los trabajos y que no se repitan
    trabajos_pks = []
    aux_trabajos_pks = []
    for i in trabajos_acordados:
        if (i.postulante_acordado.Trabajo.pk not in aux_trabajos_pks):
            aux_trabajos_pks.append(i.postulante_acordado.Trabajo.pk)
            restantes = i.postulante_acordado.Trabajo.Personas_requeridas -i.postulante_acordado.Trabajo.Vacantes
            trabajos_pks.append((i.postulante_acordado.Trabajo.pk, i.postulante_acordado.Trabajo.Nombre,i.postulante_acordado.Trabajo.Imagen,restantes,i.postulante_acordado.Trabajo.Monto_pago,i.postulante_acordado.Trabajo.Fecha,i.postulante_acordado.Trabajo.Hora))
    print("pks pegas"+str(trabajos_pks))
    print("hola")
    data['trabajos_pks'] = trabajos_pks


    # trabajos_acordados = Trabajo_acordado()
    # trabajos_acordados
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
    prueba_mail()
    enviar_email('mendrack1@gmail.com',"Prueba django dinamico","dinamico xde")
    enviar_correo_inactivos()
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    data['preferencias'] = Preferencias.objects.get(Usuario = usuario_solicitud)
    # print([i for i in Trabajo.objects.filter(Activo= 1).values('Area__Nombre').distinct()])
    areas = Trabajo.objects.filter(Activo= 1).values('Area__Nombre').distinct()
    print("hoal")
    for i in areas:
        print(i['Area__Nombre'])
    print(areas.values())
    data['areas'] = [i['Area__Nombre'] for i in Trabajo.objects.filter(Activo= 1).values('Area__Nombre').distinct()]
    data['comunas'] = [i['Direccion__Comuna__nombre'] for i in Trabajo.objects.filter(Activo=1).values('Direccion__Comuna__nombre').distinct()]
    print(data)


    # usuario = Persona.objects.get(Usuario=pk_user)

    #excluir mismo usuario
    trabajos = Trabajo.objects.filter(Activo = 1).exclude(Usuario__Usuario= usuario_solicitud)
    validar_trabajos(trabajos)
    #COMPARAR EN TEMPLATE PARA SACAR TRABAJOS A LOS QUE YA HA POSTULADO, SACA LOS TRABAJOS NO ACTIVOS....
    trabajos_postulados = Postulantes.objects.filter(Postulante = usuario_solicitud).order_by('-Fecha').exclude(Trabajo__Activo= 0)
    data['trabajos_postulados'] = trabajos_postulados
    data['trabajos'] = trabajos
    # data['usuario'] = usuario

    trabajos_listos = []
    for i in trabajos:

        if (trabajos_postulados.filter(Trabajo = i.pk)):

            #                          0    1       2               3      4       5               6             7      8        9      10
            trabajos_listos.append((i.pk,i.Nombre,i.Area.Nombre,i.Detalle,i.Fecha,i.Hora,i.Direccion.Comuna.nombre,i.Monto_pago,i.Imagen,1,i.Vacantes))
        else:
            trabajos_listos.append((i.pk,i.Nombre,i.Area.Nombre,i.Detalle,i.Fecha,i.Hora,i.Direccion.Comuna.nombre,i.Monto_pago,i.Imagen,0,i.Vacantes))

            # i.annotate(mycolumn=Value('xxx', output_field=CharField()))
            # print("si ta" + str(i.pk))
    data['prueba'] = trabajos_listos
    # print(data['trabajos'])
    #
    # print(data)
    return render(request, 'buscar_trabajo.html', data)

@login_required(login_url='/auth/login')
def h_trabajos_realizados(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    historico = Historial_trabajo.objects.filter(Persona = usuario).order_by('-Fecha','-Hora').exclude( tipo = 1)
    data["historial_trabajos_realizados"] = historico

    # print(data)
    return render(request, 'h_trabajos_realizados.html', data)

@login_required(login_url='/auth/login')
def h_trabajos_publicados(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    historico = Historial_trabajo.objects.filter(Persona = usuario).order_by('-Fecha','-Hora').exclude( tipo = 2)
    data["historial_trabajos_publicados"] = historico
    # print(usuario.pk)
    # print(request.user.pk)

    # print(data)
    return render(request, 'h_trabajos_publicados.html', data)

@login_required(login_url='/auth/login')
def detalle_trabajos_publicados(request,pk_historico):
    data = {}
    # usuario = Persona.objects.get(Usuario=pk_user)
    # data['usuario'] = usuario
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    Historico = Historial_trabajo.objects.get(pk = pk_historico)
    data['historico'] = Historico
    # historico = Historial_trabajo.objects.filter(Persona = usuario).order_by('-Fecha').exclude( tipo = 2)
    # data["historial_trabajos_publicados"] = historico
    # print(usuario.pk)
    # print(request.user.pk)
    print("PK HISTORICO"+str(pk_historico))
    postulantes = Postulantes.objects.filter(Trabajo = Historico.Trabajo).filter( Estado = 1 )
    print("postulantes: " + str(postulantes))
    for i in postulantes:
        print(i.Estado)

    data['postulantes'] = postulantes

    # print(data)
    return render(request, 'trabajos_publicados_detalle.html', data)

@login_required(login_url='/auth/login')
def detalle_trabajos_realizados(request,pk_historico):
    data = {}
    # usuario = Persona.objects.get(Usuario=pk_user)
    # data['usuario'] = usuario
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud
    Historico = Historial_trabajo.objects.get(pk = pk_historico)
    data['historico'] = Historico
    # historico = Historial_trabajo.objects.filter(Persona = usuario).order_by('-Fecha').exclude( tipo = 2)
    # data["historial_trabajos_publicados"] = historico
    # print(usuario.pk)
    # print(request.user.pk)
    print("PK HISTORICO"+str(pk_historico))
    postulantes = Postulantes.objects.filter(Trabajo = Historico.Trabajo).filter( Estado = 1 )
    print("postulantes: " + str(postulantes))
    for i in postulantes:
        print(i.Estado)

    data['postulantes'] = postulantes

    # print(data)
    return render(request, 'trabajos_realizados_detalle.html', data)
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
        # pais= request.POST['pais']
        mail = request.POST['email']
        numero_calle = request.POST['numero_calle']
        contrasena2= request.POST['confirmPassword']
        contrasena1 = request.POST['password']
        rut = request.POST['rut']
        # region = request.POST['region']
        telefono= request.POST['telefono']
        nombres = request.POST['nombres']
        # ciudad = request.POST['ciudad']
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
                persona.Nombre = nombres + ' '+apellidos
                persona.Fecha_nacimiento = f_nacimiento

                #direccion
                persona.save()
                direccion = Direccion()
                direccion.Calle = calle
                # direccion.Ciudad = ciudad
                direccion.Comuna = Comuna.objects.get(pk = comuna)
                # direccion. = Comuna.objects.get(pk = comuna)
                direccion.Numero_de_calle = numero_calle
                # direccion.Pais = pais
                direccion.Persona = persona
                direccion.save()

                # persona.Direccion = direccion




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

    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    data['regiones'] = regiones
    data['comunas'] = comunas
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
#
# @login_required(login_url='/auth/login')
# def config_perfil(request,pk_user):
#     data = {}
#     usuario = Persona.objects.get(Usuario=pk_user)
#     data['usuario'] = usuario
#
#
#     #
#     # if request.method == 'GET':
#     #     print("get")
#     # if request.method == 'POST':
#     #     #Obtengo los atributos
#     #     print("POSSST BEIBE")
#     #     print(request.POST)
#     #     print(request.FILES)
#     return render(request, 'config_perfil.html', data)
#
#     # return redirect('config_perfil', request.user.pk)
#
# @login_required(login_url='/auth/login')
# def guardar_config_perfil_redes(request,pk_user):
#     data = {}
#     usuario = Persona.objects.get(Usuario=pk_user)
#     print(usuario)
#
#     if request.method == 'GET':
#         print("get")
#     if request.method == 'POST':
#         #Obtengo los atributos
#         print("POSSST BEIBE")
#         print(request.POST)
#         print("request files")
#         # print(request.FILES)
#         print("request files fin ")
#
#         facebook = request.POST['facebook']
#         twitter = request.POST['twitter']
#         linkedin = request.POST['linkedin']
#         instagram = request.POST['instagram']
#
#         usuario.Facebook = facebook
#         usuario.Twitter = twitter
#         usuario.Linkedin = linkedin
#         usuario.Instagram = instagram
#
#         usuario.save()
#
#     # return render(request, 'visualizar_perfil.html', data)
#     return redirect('config_perfil', request.user.pk)
