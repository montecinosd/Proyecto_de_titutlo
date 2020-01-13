from django.urls import path, re_path
from Registro_fullpega import views
from Publicar_trabajo import views
from Calificaciones import views
from Configuracion_perfil import views

urlpatterns = [
     path('config_perfil/<int:pk_user>', views.config_perfil, name='config_perfil'),
     path('guardar_descripcion/<int:pk_user>', views.guardar_descripcion, name='guardar_descripcion'),
     path('config_direccion/<int:pk_direccion>', views.config_direccion, name='config_direccion'),
     path('config_direccion_actualizar/<int:pk_direccion>', views.config_direccion_actualizar, name='config_direccion_actualizar'),
     path('guardar_config_perfil_redes/<int:pk_user>', views.guardar_config_perfil_redes, name='guardar_config_perfil_redes'),
     path('guardar_config_perfil_preferencias/<int:pk_user>', views.guardar_config_perfil_preferencias, name='guardar_config_perfil_preferencias'),
     path('guardar_config_datos', views.guardar_config_datos, name='guardar_config_datos'),
     path('actualizar_contrasenha', views.actualizar_contrasenha, name='actualizar_contrasenha'),

]
