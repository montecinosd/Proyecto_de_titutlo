from django.urls import path
from Registro_fullpega import views

urlpatterns = [
     path('', views.index, name='index'),
     #pagina principal
     path('pagina_principal', views.pagina_principal, name='pagina_principal'),
     #registros
     path(r'^Registro_form', views.Registro_form, name='Registro_form'),
     path(r'^Guardar_Registro_form', views.Guardar_Registro_form, name='Guardar_Registro_form'),
     #Config perfil
     path(r'^visualizar_perfil/<int:pk_user>', views.visualizar_perfil, name='visualizar_perfil'),
     path(r'^visualizar_perfil_detalle_pega/<int:pk_pega>', views.visualizar_perfil_detalle_pega, name='visualizar_perfil_detalle_pega'),
     path(r'^config_perfil/<int:pk_user>', views.config_perfil, name='config_perfil'),
     path(r'^guardar_config_perfil_redes/<int:pk_user>', views.guardar_config_perfil_redes, name='guardar_config_perfil_redes'),
     #Privilegios
     path(r'^visualizar_privilegios/<int:pk_user>', views.visualizar_privilegios, name='visualizar_privilegios'),
     #historicos
     path(r'^h_trabajos_realizados/<int:pk_user>', views.h_trabajos_realizados, name='h_trabajos_realizados'),
     path(r'^h_trabajos_publicados/<int:pk_user>', views.h_trabajos_publicados, name='h_trabajos_publicados'),
     #buscar trabajo
     path(r'^buscar_trabajo/<int:pk_user>', views.buscar_trabajo, name='buscar_trabajo'),
     #valoraciones

]
