from django.urls import path
from Registro_fullpega import views
from sensibilidad_watson import watson


urlpatterns = [
     path('getSentimentValue', watson.getSentimentValue, name='getSentimentValue'),



]
