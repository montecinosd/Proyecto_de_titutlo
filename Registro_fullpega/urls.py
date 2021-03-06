from django.urls import path, re_path
from Registro_fullpega import views
# from Fullpega.Notificaciones_global import *
urlpatterns = [
     path('index', views.index, name='index'),
     #pagina principal
     path('', views.pagina_principal, name='pagina_principal'),
     #registros
     path('Registro_form', views.Registro_form, name='Registro_form'),
     path('Guardar_Registro_form', views.Guardar_Registro_form, name='Guardar_Registro_form'),
     #Config perfil
     path('visualizar_perfil/<int:pk_user>', views.visualizar_perfil, name='visualizar_perfil'),
     path('visualizar_perfil_detalle_pega/<int:pk_pega>', views.visualizar_perfil_detalle_pega, name='visualizar_perfil_detalle_pega'),
     # path('config_perfil/<int:pk_user>', views.config_perfil, name='config_perfil'),
     # path('guardar_config_perfil_redes/<int:pk_user>', views.guardar_config_perfil_redes, name='guardar_config_perfil_redes'),
     #Privilegios
     path('visualizar_privilegios/<int:pk_user>', views.visualizar_privilegios, name='visualizar_privilegios'),
     #historicos
     path('h_trabajos_realizados/<int:pk_user>', views.h_trabajos_realizados, name='h_trabajos_realizados'),
     path('h_trabajos_publicados/<int:pk_user>', views.h_trabajos_publicados, name='h_trabajos_publicados'),
     path('detalle_trabajos_publicados/<int:pk_historico>', views.detalle_trabajos_publicados, name='detalle_trabajos_publicados'),
     path('detalle_trabajos_realizados/<int:pk_historico>', views.detalle_trabajos_realizados, name='detalle_trabajos_realizados'),

     #buscar trabajo
     path('buscar_trabajo/<int:pk_user>', views.buscar_trabajo, name='buscar_trabajo'),
     #Postular
     path('postular_inicial/<int:pk_pega>', views.postular_inicial, name='postular_inicial'),
     #v_ postulantes
     path('visualizar_postulantes_a_trabajos/<int:pk_user>', views.visualizar_postulantes_a_trabajos, name='visualizar_postulantes_a_trabajos'),
     path('visualizar_postulantes_detalle/<int:pk_pega>', views.visualizar_postulantes_detalle, name='visualizar_postulantes_detalle'),
     path('visualizar_postulantes_detalle_watson/<int:pk_pega>', views.visualizar_postulantes_detalle_watson, name='visualizar_postulantes_detalle_watson'),
     path('visualizar_perfil_postulante/<int:pk_postulante>', views.visualizar_perfil_postulante, name='visualizar_perfil_postulante'),
   #
     path('postulante_acordado/<int:pk_postulante>', views.postulante_acordado, name='postulante_acordado'),
     path('visualizar_trabajo_activo/<int:pk_user>', views.visualizar_trabajo_activo, name='visualizar_trabajo_activo'),

     #cierre
     path('cerrar_trabajo_publicado/<int:pk_trabajo>', views.cerrar_trabajo_publicado,name='cerrar_trabajo_publicado'),
     path('calificar_oferente/<int:pk_notificacion>', views.calificar_oferente,name='calificar_oferente'),

     #valoraciones

]
