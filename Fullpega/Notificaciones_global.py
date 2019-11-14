
from Publicar_trabajo.models import *
from Registro_fullpega.models import *
from Auth_fullpega.models import *

def get_notificaciones(request):
	# data = {}
	#si no hay usuario
	try:
		if(request.user.pk == None):
			return ""
		else:
			usuario_solicitud = Persona.objects.get(Usuario=request.user.pk)
			# data['usuario_solicitud'] = usuario_solicitud
			notificaciones = Notificaciones.objects.filter(usuario=usuario_solicitud).exclude(Activo = 0).order_by('-Fecha')
			# for i in notificaciones:
				# print(i.Activo)


			return {'notificaciones':notificaciones}
	except:
		return ""