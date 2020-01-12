from django.urls import path, re_path
from Registro_fullpega import views
from Publicar_trabajo import views
from Calificaciones import views
urlpatterns = [
     re_path(r'^visualizar_calificar_pegas/<int:pk_user>', views.visualizar_calificar_pegas, name='visualizar_calificar_pegas'),
     re_path(r'^terminar_calificacion/<int:pk_calificacion>', views.terminar_calificacion, name='terminar_calificacion'),

]
