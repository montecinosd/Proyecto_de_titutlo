from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('Registro_fullpega.urls'), name='Registro_fullpega'),
    path('auth/', include('Auth_fullpega.urls'), name='auth'),
    path('publicar/', include('Publicar_trabajo.urls'), name='auth'),
    path('', include('sensibilidad_watson.urls'),name="watson")

    # path("index_Fullpega/", include('Fullpega.urls'), name='Fullpega'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
