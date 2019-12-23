from django.urls import path
from Registro_fullpega import views
from sensibilidad_watson import watson,twitter
from django.urls import path


urlpatterns = [
     path('getSentimentValue', watson.getSentimentValue, name='getSentimentValue'),
     path('install/', watson.install, name="install"),
     path('summary/', watson.getResultSummary, name="getResultSummary"),
     path('chart_twitter/<int:pk_user>', watson.chartsSummaries_twitter, name="chartsSummaries_twitter"),
     path('chart/<int:pk_user>', watson.chartsSummaries, name="chartsSummaries"),
     path('chart_texto_twiiter/<int:pk_user>', watson.chartsSummaries_texto_twitter, name="chartsSummaries_texto_twitter"),
     path('twitter/', twitter.prueba, name="prueba"),
     # path('historic/', watson.historic_summary, name="historic_summary"),

     # path(r'getSentimentValue/<int:pk_usuario>', watson.getSentimentValue, name='getSentimentValue'),
     # path(r'^calificar_oferente/<int:pk_notificacion>', views.calificar_oferente, name='calificar_oferente'),

]
