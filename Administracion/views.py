
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Publicar_trabajo.models import *
from sensibilidad_watson.watson import *
from sensibilidad_watson.twitter import *
from django.db.models import Count, Avg
from django.utils import timezone
from django.db.models import F
import datetime
from sensibilidad_watson import views
from Correos.views import *
def convertir_segundos(seg):
    # print(seg)
    if (seg<60):
        return str(seg)+' seg'
    elif(seg>=60 and seg<3600):

        return str(int(seg/60))+' min '+str(int((seg%60))) + ' seg'
    elif(seg>=3600):
        return str(int(seg/3600))+' dia '+str(int((seg%3600)/60))+' min'

# Create your views here.
@login_required(login_url='/auth/login')
def index_admin(request):
    # Ejecutar solo por primera vez para instalar regiones y comunas
    # instalar_regiones_comunas(request)
    #get_personality("Estoy loco Yo ya no puedo entender La gente esta tan dura Que ya no se puede creer Voy buscando Algo no me importa que Que tengan algún lado Algo que al menos venga bien Cruzando la esquina Te veo y vuelvo recordar Aquella medicina Que nos gustaba saborear De hecho esta vacía Me escapo solo a caminar Soliendome la vida Te veo y vuelvo a empezar Si te estas sintiendo sola Me puedes venir a ver Hace tiempo fuiste mi amor")
    # install(request) #instalar categiorias
    # print("hola")
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)

    # instalar_regiones_comunas(request)
    if(request.POST):
        print(request.POST)
        print(type(request.POST.get("fecha_inicio")[8:10]))
        fecha_ini = request.POST.get("fecha_inicio")
        fecha_ini = datetime.datetime(int(fecha_ini[0:4]),int(fecha_ini[5:7]),int(fecha_ini[8:10]))
        fecha_fin = request.POST.get("fecha_fin")
        fecha_fin = datetime.datetime(int(fecha_fin[0:4]),int(fecha_fin[5:7]),int(fecha_fin[8:10]))
    else:
        fecha_ini = datetime.datetime(2018,int("01"),16)
        fecha_fin = datetime.datetime(2050,1,16)
    # print("hola")
    print(fecha_ini)

    data = {}
    # install(request)
    # c = prueba(request, usuario_solicitud.Twitter)
    # b= getResultSummary(request,c)
    # print(b)
    data['usuario_solicitud'] = Persona.objects.get(pk = request.user.pk)
    usuarios = User.objects.filter(is_staff = False) #todos los usuarios normales'
    data['usuarios'] = usuarios
    comunas_pega = Trabajo.objects.filter(Fecha_publicacion__range=(fecha_ini,fecha_fin)).values("Direccion__Comuna").distinct()
    data['comunas_pega'] = comunas_pega
    trabajos = Trabajo.objects.filter(Activo = 1)
    data['trabajos'] = trabajos
    data['calificaciones'] = Calificaciones.objects.filter(Fecha__range=(fecha_ini,fecha_fin))
    calificacion5 = Calificaciones.objects.filter(Estrellas = 5)
    calificacion4 = Calificaciones.objects.filter(Estrellas = 4)
    calificacion3 = Calificaciones.objects.filter(Estrellas = 3)
    calificacion2 = Calificaciones.objects.filter(Estrellas = 2)
    calificacion1 = Calificaciones.objects.filter(Estrellas = 1)
    # print(calificacion5)
    # print(calificacion4)
    # print(calificacion3)
    # print(calificacion2)
    # print(calificacion1)
    data['calificacion5']=calificacion5
    data['calificacion4']=calificacion4
    data['calificacion3']=calificacion3
    data['calificacion2']=calificacion2
    data['calificacion1']=calificacion1
    # vacia = Trabajo.objects.none()
    # print(vacia)
    comunas_frecuentes = Trabajo.objects.filter(Fecha_publicacion__range=(fecha_ini,fecha_fin)).values("Direccion__Comuna__nombre").annotate(count=Count('Direccion__Comuna')).order_by("-count")
    data['comunas_frecuentes'] = comunas_frecuentes

    areas_frecuentes = Trabajo.objects.filter(Fecha_publicacion__range=(fecha_ini,fecha_fin)).values("Area__Nombre").annotate(count=Count('Area__Nombre')).order_by("-count")
    print(areas_frecuentes)
    data['areas_frecuentes'] = areas_frecuentes

    # rellena = comunas_frecuentes|vacia
    # print(rellena)
    rango_horario = Trabajo.objects.filter(Fecha_publicacion__range=(fecha_ini,fecha_fin))
    horas_1_8 = [r for r in rango_horario if 1 <= (timezone.localtime(r.Fecha)).hour < 8] #1 a 7:59
    horas_8_12 = [r for r in rango_horario if 8 <= (timezone.localtime(r.Fecha)).hour < 12]#8 a 11:59
    horas_12_16 = [r for r in rango_horario if 12 <= (timezone.localtime(r.Fecha)).hour < 16]#12 a 15:59
    horas_16_20 = [r for r in rango_horario if 16 <= (timezone.localtime(r.Fecha)).hour < 20]#16 a 19:59
    horas_20_24 = [r for r in rango_horario if 20 <= (timezone.localtime(r.Fecha)).hour <= 24 or (timezone.localtime(r.Fecha)).hour == 0]#20 a 24:59
    # for i in rango_horario:
    #     print((timezone.localtime(i.Fecha)).hour)
        # print(i.Fecha.hour)
    # print(horas_1_8)
    # print(horas_8_12)
    # print(horas_12_16)
    # print(horas_16_20)
    # print(horas_20_24)
    data['horas_1_8'] = horas_1_8
    data['horas_8_12'] = horas_8_12
    data['horas_12_16'] = horas_12_16
    data['horas_16_20'] = horas_16_20
    data['horas_20_24'] = horas_20_24
    # print(comunas_frecuentes)
    # print(usuarios)
    # usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    # data['usuario_solicitud'] = usuario_solicitud
    postulantes_totales = Postulantes.objects.all()

    diferencias_fechas = []
    for i in postulantes_totales:
        fi = i.Trabajo.Fecha_publicacion
        ff = i.Fecha
        dif = ff-fi
        diferencias_fechas.append((dif))
    sum = 0

    for i in diferencias_fechas:
        sum = sum + i.total_seconds()
    prom_dif = sum/len(diferencias_fechas)
    final_dif = convertir_segundos(prom_dif)

    data['final_dif'] = final_dif

    return render(request, 'index_admin.html', data)

def correos_areas_solicitadas(request):
    data = {}
    correos = []
    today = datetime.date.today()
    pasado = today - datetime.timedelta(days=4)

    areas_frecuentes = Trabajo.objects.filter(Fecha_publicacion__range=(pasado,today)).values("Area__Nombre").annotate(count=Count('Area__Nombre')).order_by("-count")
    cont=0
    aux=False
    for i in areas_frecuentes:
        print(i)
        if cont == 5:
            break
        if (Preferencias.objects.filter(Area = Areas.objects.get(Nombre=i['Area__Nombre']))):
            aux = True
            personas = Preferencias.objects.filter(Area = Areas.objects.get(Nombre=i['Area__Nombre']))[5]
            correos_aux = [i.Correo for i in personas]
            correos = correos + correos_aux
        cont=cont+1
    print(correos)
    if(aux):
        enviar_emails("Pegas acumuladas en FP!", "Conectate y genera! FullPega te está esperando ;)", correos)
    return render(request, 'enviar_correos.html', data)


def correos_usuarios_inactivos(request):
    data={}
    start_date = datetime.date(2019, 1, 1)
    today = datetime.date.today()
    semana_pasada = today - datetime.timedelta(days=7)
    # User.objects.filter(last_login__range=(start_date, end_date))
    if (Persona.objects.filter(Usuario__last_login__range=(start_date,semana_pasada))):
        personas = Persona.objects.filter(Usuario__last_login__range=(start_date,semana_pasada))[25]
        correos = [i.Correo for i in personas]
        enviar_emails("Conectate y vuelve a FullPega!", "Las mejores pegas para ti, están en fullpega, encuentra a alguien que haga una pega por ti o encuentra la pega perfecta ;), vuelve a Fullpega!", correos)

    return render(request, 'enviar_correos.html', data)

def instalar_regiones_comunas(request):
    uwu = [{'region': "Aisén del Gral. Carlos Ibáñez del Campo",
            'comunas': ["Aisén", "Chile Chico", "Cisnes", "Cochrane", "Coihaique", "Guaitecas", "Lago Verde",
                        "O’Higgins", "Río Ibáñez", "Tortel"]},
           {'region': "Antofagasta",
            'comunas': ["Antofagasta", "Calama", "María Elena", "Mejillones", "Ollagüe", "San Pedro de Atacama",
                        "Sierra Gorda", "Taltal", "Tocopilla"]},
           {'region': "Arica y Parinacota",
            'comunas': ["Arica", "Camarones", "General Lagos", "Putre"]},
           {'region': "Atacama",
            'comunas': ["Alto del Carmen", "Caldera", "Chañaral", "Copiapó", "Diego de Almagro", "Freirina", "Huasco",
                        "Tierra Amarilla", "Vallenar"]},
           {'region': "Biobío",
            'comunas': ["Alto Biobío", "Antuco", "Arauco", "Cabrero", "Cañete", "Chiguayante", "Concepción", "Contulmo",
                        "Coronel", "Curanilahue", "Florida", "Hualpén", "Hualqui", "Laja", "Lebu", "Los Álamos",
                        "Los Ángeles", "Lota", "Mulchén", "Nacimiento", "Negrete", "Penco", "Quilaco", "Quilleco",
                        "San Pedro de la Paz", "San Rosendo", "Santa Bárbara", "Santa Juana", "Talcahuano", "Tirúa",
                        "Tomé", "Tucapel", "Yumbel"]},
           {'region': "Coquimbo",
            'comunas': ["Andacollo", "Canela", "Combarbalá", "Coquimbo", "Illapel", "La Higuera", "La Serena",
                        "Los Vilos", "Monte Patria", "Ovalle", "Paiguano", "Punitaqui", "Río Hurtado", "Salamanca",
                        "Vicuña"]},
           {'region': "La Araucanía",
            'comunas': ["Angol", "Carahue", "Cholchol", "Collipulli", "Cunco", "Curacautín", "Curarrehue", "Ercilla",
                        "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Lonquimay", "Los Sauces", "Lumaco",
                        "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Purén",
                        "Renaico", "Saavedra", "Temuco", "Teodoro Schmidt", "Toltén", "Traiguén", "Victoria", "Vilcún",
                        "Villarrica"]},
           {'region': "Libertador Gral. Bernardo O’Higgins",
            'comunas': ["Chépica", "Chimbarongo", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "La Estrella",
                        "Las Cabras", "Litueche", "Lolol", "Machalí", "Malloa", "Marchihue", "Mostazal", "Nancagua",
                        "Navidad", "Olivar", "Palmilla", "Paredones", "Peralillo", "Peumo", "Pichidegua", "Pichilemu",
                        "Placilla", "Pumanque", "Quinta de Tilcoco", "Rancagua", "Rengo", "Requínoa", "San Fernando",
                        "San Vicente", "Santa Cruz"]},
           {'region': "Los Lagos",
            'comunas': ["Ancud", "Calbuco", "Castro", "Chaitén", "Chonchi", "Cochamó", "Curaco de Vélez", "Dalcahue",
                        "Fresia", "Frutillar", "Futaleufú", "Hualaihué", "Llanquihue", "Los Muermos", "Maullín",
                        "Osorno", "Palena", "Puerto Montt", "Puerto Octay", "Puerto Varas", "Puqueldón", "Purranque",
                        "Puyehue", "Queilén", "Quellón", "Quemchi", "Quinchao", "Río Negro", "San Juan de la Costa",
                        "San Pablo"]},
           {'region': "Los Ríos",
            'comunas': ["Corral", "Futrono", "La Unión", "Lago Ranco", "Lanco", "Los Lagos", "Máfil", "Mariquina",
                        "Paillaco", "Panguipulli", "Río Bueno", "Valdivia"]},
           {'region': "Magallanes y de la Antártica Chilena",
            'comunas': ["Antártica", "Cabo de Hornos (Ex Navarino)", "Laguna Blanca", "Natales", "Porvenir",
                        "Primavera", "Punta Arenas", "Río Verde", "San Gregorio", "Timaukel", "Torres del Paine"]},
           {'region': "Maule",
            'comunas': ["Cauquenes", "Chanco", "Colbún", "Constitución", "Curepto", "Curicó", "Empedrado", "Hualañé",
                        "Licantén", "Linares", "Longaví", "Maule", "Molina", "Parral", "Pelarco", "Pelluhue",
                        "Pencahue", "Rauco", "Retiro", "Río Claro", "Romeral", "Sagrada Familia", "San Clemente",
                        "San Javier", "San Rafael", "Talca", "Teno", "Vichuquén", "Villa Alegre", "Yerbas Buenas"]},
           {'region': "Metropolitana de Santiago",
            'comunas': ["Alhué", "Buin", "Calera de Tango", "Cerrillos", "Cerro Navia", "Colina", "Conchalí",
                        "Curacaví", "El Bosque", "El Monte", "Estación Central", "Huechuraba", "Independencia",
                        "Isla de Maipo", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Lampa",
                        "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "María Pinto",
                        "Melipilla", "Ñuñoa", "Padre Hurtado", "Paine", "Pedro Aguirre Cerda", "Peñaflor", "Peñalolén",
                        "Pirque", "Providencia", "Pudahuel", "Puente Alto", "Quilicura", "Quinta Normal", "Recoleta",
                        "Renca", "San Bernardo", "San Joaquín", "San José de Maipo", "San Miguel", "San Pedro",
                        "San Ramón", "Santiago", "Talagante", "Tiltil", "Vitacura"]},
           {'region': "Ñuble",
            'comunas': ["Bulnes", "Chillán", "Chillán Viejo", "Cobquecura", "Coelemu", "Coihueco", "El Carmen",
                        "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil",
                        "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"]},
           {'region': "Tarapacá",
            'comunas': ["Alto Hospicio", "Camiña", "Colchane", "Huara", "Iquique", "Pica", "Pozo Almonte"]},
           {'region': "Valparaíso",
            'comunas': ["Algarrobo", "Cabildo", "Calera", "Calle Larga", "Cartagena", "Casablanca", "Catemu", "Concón",
                        "El Quisco", "El Tabo", "Hijuelas", "Isla de Pascua", "Juan Fernández", "La Cruz", "La Ligua",
                        "Limache", "Llaillay", "Los Andes", "Nogales", "Olmué", "Panquehue", "Papudo", "Petorca",
                        "Puchuncaví", "Putaendo", "Quillota", "Quilpué", "Quintero", "Rinconada", "San Antonio",
                        "San Esteban", "San Felipe", "Santa María", "Santo Domingo", "Valparaíso", "Villa Alemana",
                        "Viña del Mar", "Zapallar"]}]
    print(type(uwu))
    for x in uwu:
        region_obj = Region.objects.create(nombre=x['region'])
        for i in x['comunas']:
            region_obj.add_commune(i)
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
def enviar_correos(request):
    data={}
    if (request.POST):
        print("Post")
        asunto =request.POST.get("asunto")
        mensaje=request.POST.get("mensaje")

        print(asunto)
        print(mensaje)
        personas = Persona.objects.all()
        correos = [i.Correo for i in personas]
        enviar_emails(asunto,mensaje,correos)
        print(personas)
        # correos = [i. for i in Persona.objects.all]
        return render(request, 'enviar_correos.html', data)

    else:
      return render(request, 'enviar_correos.html', data)
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

#deshabilitar pega
@login_required(login_url='/auth/login')
def deshabilitar_pega_adm(request,pk_pega):
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    pega = Trabajo.objects.get(pk = pk_pega)

    if(pega.Activo == 1):
        pega.Activo = 0
        pega.save()
    else:
        pega.Activo = 1
        pega.save()

    return redirect('adm_pegas')

#deshabilitar pega
@login_required(login_url='/auth/login')
def deshabilitar_user_adm(request,pk_user):
    data = {}
    usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    data['usuario_solicitud'] = usuario_solicitud

    user = User.objects.get(pk = pk_user)


    if(user.is_active == True):
        user.is_active = False
        user.save()
    else:
        user.is_active = True
        user.save()

    return redirect('adm_usuarios')