from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Registro_fullpega.urls'), name='Registro_fullpega'),
    path('auth/', include('Auth_fullpega.urls'), name='auth'),
    path('publicar/', include('Publicar_trabajo.urls'), name='Publicar'),
    path('calificar/', include('Calificaciones.urls'), name='Calificar'),
    path('configuracion/', include('Configuracion_perfil.urls'), name='configuracion'),
    path('administracion/', include('Administracion.urls'), name='administracion'),
    path('', include('sensibilidad_watson.urls'),name="watson")

    # path("index_Fullpega/", include('Fullpega.urls'), name='Fullpega'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
