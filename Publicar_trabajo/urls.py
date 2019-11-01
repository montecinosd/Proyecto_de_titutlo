from django.urls import path
from Registro_fullpega import views
from Publicar_trabajo import views

urlpatterns = [
     path('publicar_trabajo', views.publicar_trabajo, name='publicar_trabajo'),
     path('publicar_trabajo/<int:pk_user>', views.publicar_trabajo, name='publicar_trabajo'),
     path(r'^guardar_trabajo/<int:pk_user>', views.guardar_trabajo, name='guardar_trabajo'),

]
