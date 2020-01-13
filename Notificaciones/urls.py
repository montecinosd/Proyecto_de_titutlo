from Notificaciones import views
from django.urls import path
urlpatterns = [
     path('', views.apagar_notificaciones, name='apagar_notificaciones'),

]
