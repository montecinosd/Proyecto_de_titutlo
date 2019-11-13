import json

from django.http import JsonResponse
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

from Registro_fullpega.models import *
from Publicar_trabajo.models import *
from django.db.models import Avg

from Registro_fullpega.models import Historico_watson


def getSentimentValue(request, **kwargs):
	print(request)
	print(type(str(request)))
	try:
		# if(kwargs['pk_user']):
		print("FUNCIONA!!!")
		pk_user = kwargs['pk_user']
	except:
		str_request = str(request)


		index = str_request.index('pk_user=')+8

		# print("Substring 'is fun':", index)
		print("Substring 'is fun':", str_request[index])

		# for i in range(10):
		# 	if(str_request[index+i].isdigit()):
		# 		print("hola")
		# 	else:
		# 		print("no es str")
		# 		print(str_request[index+i])
		pk_user = str_request[index:len(str_request)-2]
		print("PK FINALISIMO"+str(pk_user))

	# print(request.pk_user)
	# print(json.loads(request.body))
	usuario = Persona.objects.get(Usuario=pk_user)
	calificaciones = Calificaciones.objects.filter(usuario = usuario).exclude(Comentarios = '-')
	print(calificaciones)
	text = ''
	for i in calificaciones:
		print(i.Comentarios)
		text = text + str(i.Comentarios) + ' - '
	sentiment = 0
	try:
		natural_language_understanding = NaturalLanguageUnderstandingV1(
			version='2018-11-16',
			iam_apikey='aBNzdAKi968PRJ32n-s37yGllvpuNK5sDlRGPSS7Kphe',
			url='https://gateway.watsonplatform.net/natural-language-understanding/api'
		)

		word_len = []
		print("TEXTO DE WATSON: ", text)
		phrase = text
		txt = phrase.replace(",", "").replace(".", "").split(" ")
		n = 3
		for x in txt:
			if len(x) > n:
				print("Frase clave: ", x)
				word_len.append(x)

		response = natural_language_understanding.analyze(
			text=phrase,
			features=Features(sentiment=SentimentOptions(targets=word_len))).get_result()
		print(response)
		emotionScore = float(json.dumps(response['sentiment']['document']['score'], indent=2)) * 100
		# emotionLabel = (json.dumps(response['sentiment']['document']['label'], indent=2))
		# print(emotionLabel)
		sentiment = round(emotionScore, 1)
		satisfaction = ""
		if sentiment >= 90:
			satisfaction = 'Excelente'
		elif sentiment > 49.9 and sentiment < 90:
			satisfaction = 'Bueno'

		elif sentiment <= 49.9 and sentiment >= 0:
			satisfaction = 'Neutral'
		else:
			satisfaction = 'Malo'

		prom_estrellas = Calificaciones.objects.filter(usuario = usuario).aggregate(Avg('Estrellas'))
		print("PROM EST: "+str(prom_estrellas))
		aux_estrellas = prom_estrellas['Estrellas__avg']
		usuario = Persona.objects.get( pk = pk_user)
		usuario.Puntaje_watson = sentiment
		usuario.Label_watson = satisfaction
		print("ASDAS+"+str(aux_estrellas))
		# usuario.Estrellas = '5.0'
		usuario.save()
		print("hola")
		historial_watson = Historico_watson()  # type: Historico_watson
		print("hola2")
		historial_watson.Usuario = usuario
		historial_watson.Puntaje = sentiment
		print("hola3")
		historial_watson.Label = satisfaction
		print("hola4")
		historial_watson.save()
		print("hola5")


		print("Nivel de sentiminento: ", sentiment)
		print("Clasificación usuario: ", satisfaction)
	except:
		print("No se pudo obtener la información de Watson")
		sentiment = 5
		data = {
			'sentimiento': 'El usuario aún no cuenta con comentarios respecto a sus pegas',
			'satisfaccion': 'El usuario aún no cuenta con comentarios respecto a sus pegas'
		}
		return JsonResponse(data)

	data = {
		'sentimiento': sentiment,
		'satisfaccion': satisfaction
	}

	return JsonResponse(data)
	# return (sentiment)
