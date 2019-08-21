from django.urls import path
from Registro_fullpega import views

urlpatterns = [
     path('', views.index, name='index'),
     path('pagina_principal', views.pagina_principal, name='pagina_principal'),
     path('Registro', views.Registro_form, name='Registro_form'),
     path(r'^visualizar_perfil/<int:pk_user>', views.visualizar_perfil, name='visualizar_perfil'),
     path(r'^visualizar_privilegios/<int:pk_user>', views.visualizar_privilegios, name='visualizar_privilegios'),
     path(r'^h_trabajos_realizados/<int:pk_user>', views.h_trabajos_realizados, name='h_trabajos_realizados'),
     path(r'^h_trabajos_publicados/<int:pk_user>', views.h_trabajos_publicados, name='h_trabajos_publicados'),
     path(r'^buscar_trabajo/<int:pk_user>', views.buscar_trabajo, name='buscar_trabajo'),

]
