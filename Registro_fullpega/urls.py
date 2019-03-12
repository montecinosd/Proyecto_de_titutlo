from django.urls import path
from Registro_fullpega import views

urlpatterns = [
     path('', views.index, name='index'),
     path('Registro', views.Registro_form, name='Registro_form'),
]
