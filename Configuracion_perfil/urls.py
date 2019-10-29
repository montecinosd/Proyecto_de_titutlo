from django.urls import path
from Registro_fullpega import views
from Publicar_trabajo import views
from Calificaciones import views
from Configuracion_perfil import views

urlpatterns = [
     path(r'^config_perfil/<int:pk_user>', views.config_perfil, name='config_perfil'),
     path(r'^guardar_config_perfil_redes/<int:pk_user>', views.guardar_config_perfil_redes, name='guardar_config_perfil_redes'),

]
