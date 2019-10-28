from django.urls import path
from Registro_fullpega import views
from Publicar_trabajo import views
from Calificaciones import views
urlpatterns = [
     path(r'^visualizar_calificar_pegas/<int:pk_user>', views.visualizar_calificar_pegas, name='visualizar_calificar_pegas'),

]
