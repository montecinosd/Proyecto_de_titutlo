from django.urls import path, re_path
from Registro_fullpega import views
from Publicar_trabajo import views
from Calificaciones import views
from Administracion import views
urlpatterns = [
     path('index_admin', views.index_admin, name='index_admin'),
     path('adm_usuarios', views.adm_usuarios, name='adm_usuarios'),
     path('adm_pegas', views.adm_pegas, name='adm_pegas'),
     path('enviar_correos', views.enviar_correos, name='enviar_correos'),
     re_path(r'^  visualizar_perfil_adm/<int:pk_user>', views.visualizar_perfil_adm, name='visualizar_perfil_adm'),
     re_path(r'^  visualizar_pega_adm/<int:pk_pega>', views.visualizar_pega_adm, name='visualizar_pega_adm'),
     re_path(r'^  deshabilitar_pega_adm/<int:pk_pega>', views.deshabilitar_pega_adm, name='deshabilitar_pega_adm'),
     re_path(r'^  deshabilitar_user_adm/<int:pk_user>', views.deshabilitar_user_adm, name='deshabilitar_user_adm'),

]
