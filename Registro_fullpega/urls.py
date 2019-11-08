from django.urls import path
from Registro_fullpega import views


urlpatterns = [
     path('index', views.index, name='index'),
     #pagina principal
     path('', views.pagina_principal, name='pagina_principal'),
     #registros
     path(r'^Registro_form', views.Registro_form, name='Registro_form'),
     path(r'^Guardar_Registro_form', views.Guardar_Registro_form, name='Guardar_Registro_form'),
     #Config perfil
     path(r'^visualizar_perfil/<int:pk_user>', views.visualizar_perfil, name='visualizar_perfil'),
     path(r'^visualizar_perfil_detalle_pega/<int:pk_pega>', views.visualizar_perfil_detalle_pega, name='visualizar_perfil_detalle_pega'),
     # path(r'^config_perfil/<int:pk_user>', views.config_perfil, name='config_perfil'),
     # path(r'^guardar_config_perfil_redes/<int:pk_user>', views.guardar_config_perfil_redes, name='guardar_config_perfil_redes'),
     #Privilegios
     path(r'^visualizar_privilegios/<int:pk_user>', views.visualizar_privilegios, name='visualizar_privilegios'),
     #historicos
     path(r'^h_trabajos_realizados/<int:pk_user>', views.h_trabajos_realizados, name='h_trabajos_realizados'),
     path(r'^h_trabajos_publicados/<int:pk_user>', views.h_trabajos_publicados, name='h_trabajos_publicados'),
     #buscar trabajo
     path(r'^buscar_trabajo/<int:pk_user>', views.buscar_trabajo, name='buscar_trabajo'),
     #Postular
     path(r'^postular_inicial/<int:pk_pega>', views.postular_inicial, name='postular_inicial'),
     #v_ postulantes
     path(r'^visualizar_postulantes_a_trabajos/<int:pk_user>', views.visualizar_postulantes_a_trabajos, name='visualizar_postulantes_a_trabajos'),
     path(r'^visualizar_postulantes_detalle/<int:pk_pega>', views.visualizar_postulantes_detalle, name='visualizar_postulantes_detalle'),
     path(r'^visualizar_perfil_postulante/<int:pk_postulante>', views.visualizar_perfil_postulante, name='visualizar_perfil_postulante'),
   #
     path(r'^postulante_acordado/<int:pk_postulante>', views.postulante_acordado, name='postulante_acordado'),
     path(r'^visualizar_trabajo_activo/<int:pk_user>', views.visualizar_trabajo_activo, name='visualizar_trabajo_activo'),

     #cierre
     path(r'^cerrar_trabajo_publicado/<int:pk_trabajo>', views.cerrar_trabajo_publicado,name='cerrar_trabajo_publicado'),
     path(r'^calificar_oferente/<int:pk_notificacion>', views.calificar_oferente,name='calificar_oferente'),

     #valoraciones

]
