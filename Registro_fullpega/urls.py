from django.urls import path
from Registro_fullpega import views

urlpatterns = [
     path('', views.index, name='index'),
]
