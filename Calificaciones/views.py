from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Publicar_trabajo.models import *

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

