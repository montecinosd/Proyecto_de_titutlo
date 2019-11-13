from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Publicar_trabajo.models import *
from sensibilidad_watson.watson import *

# Create your views here.
@login_required(login_url='/auth/login')
def visualizar_calificar_pegas(request, pk_user):
	print("hola")
	data = {}
	usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
	data['usuario_solicitud'] = usuario_solicitud

	calificaciones_pendientes = Calificaciones.objects.filter(usuario_calificador = usuario_solicitud).exclude(Realizada = 1)
	print(calificaciones_pendientes)
	data['calificaciones_pendientes'] = calificaciones_pendientes

	return render(request, 'calificar_usuarios.html', data)

@login_required(login_url='/auth/login')
def terminar_calificacion(request, pk_calificacion):

	print("hola")
	data = {}
	usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
	data['usuario_solicitud'] = usuario_solicitud

	calificacion = Calificaciones.objects.get( pk = pk_calificacion)
	print(calificacion)

	# request.POST = request.POST.copy()
	# request.POST['pk_user'] = calificacion.usuario.pk
	# watson = getSentimentValue(request, pk_user=calificacion.usuario.pk)
	# print(watson)
	#

	estrellas = request.POST['stars']
	comentarios = request.POST['comentario']

	calificacion.Comentarios = comentarios
	calificacion.Estrellas = estrellas
	calificacion.Realizada = 1
	calificacion.save()
	watson = getSentimentValue(request, pk_user=calificacion.usuario.pk)
	print(watson)


# redirijo a la funcion de arriba
	return redirect('visualizar_calificar_pegas',request.user.pk)