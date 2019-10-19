from django.urls import path
from Registro_fullpega import views
from sensibilidad_watson import watson


urlpatterns = [
     path('getSentimentValue', watson.getSentimentValue, name='getSentimentValue'),
     # path(r'getSentimentValue/<int:pk_usuario>', watson.getSentimentValue, name='getSentimentValue'),
     # path(r'^calificar_oferente/<int:pk_notificacion>', views.calificar_oferente, name='calificar_oferente'),

]
