from django.urls import path, re_path
from Registro_fullpega import views
from Publicar_trabajo import views
from Calificaciones import views
from Configuracion_perfil import views

urlpatterns = [
     re_path(r'^config_perfil/<int:pk_user>', views.config_perfil, name='config_perfil'),
     re_path(r'^guardar_descripcion/<int:pk_user>', views.guardar_descripcion, name='guardar_descripcion'),
     re_path(r'^config_direccion/<int:pk_direccion>', views.config_direccion, name='config_direccion'),
     re_path(r'^config_direccion_actualizar/<int:pk_direccion>', views.config_direccion_actualizar, name='config_direccion_actualizar'),
     re_path(r'^guardar_config_perfil_redes/<int:pk_user>', views.guardar_config_perfil_redes, name='guardar_config_perfil_redes'),
     re_path(r'^guardar_config_perfil_preferencias/<int:pk_user>', views.guardar_config_perfil_preferencias, name='guardar_config_perfil_preferencias'),
     path('guardar_config_datos', views.guardar_config_datos, name='guardar_config_datos'),
     path('actualizar_contrasenha', views.actualizar_contrasenha, name='actualizar_contrasenha'),

]
