import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions


def getSentimentValue(text):
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
		if sentiment >= 90:
			satisfaction = 'Excelente'
		elif sentiment > 49.9 and sentiment < 90:
			satisfaction = 'Bueno'

		elif sentiment <= 49.9 and sentiment >= 0:
			satisfaction = 'Neutral'
		else:
			satisfaction = 'Malo'

		print("Nivel de sentiminento: ", sentiment)
		print("Clasificación usuario: ", satisfaction)
	except:
		print("No se pudo obtener la información de Watson")
		sentiment = 5
	return (sentiment)
