
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
    # usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
    # data['usuario_solicitud'] = usuario_solicitud
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
        region_obj = Region.objects.create(name=x['region'])
        for i in x['comunas']:
            region_obj.add_commune(i)
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