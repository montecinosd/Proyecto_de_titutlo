import json
from os.path import join, dirname

from django.http import JsonResponse
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
from django.shortcuts import render, redirect

from Registro_fullpega.models import *
from Publicar_trabajo.models import *
from django.db.models import Avg
from sensibilidad_watson.models import *
from Registro_fullpega.models import Historico_watson

from watson_developer_cloud import PersonalityInsightsV3
from sensibilidad_watson.twitter import *
# Watson API KEYS

API_URI = 'https://gateway.watsonplatform.net/personality-insights/api'
API_KEY = 'qpPxOSBZchJRbLiEuzkUGug7rOALlB0IEs6-YLXR_YkF'


def get_personality(data_text):
    print(data_text)
    service = PersonalityInsightsV3(
        version='2017-10-13',
        url=API_URI,
        iam_apikey=API_KEY)

    profile = service.profile(
        data_text,
        content_type='text/plain;charset=utf-8',
        content_language='es',
        accept_language='es',
        raw_scores=True,
        consumption_preferences=False).get_result()

    print(profile)

    return profile


def install(request):
    response = {}

    with open(join(dirname(__file__), 'profile_test.txt')) as profile_json:
        profile = get_personality(profile_json.read())
        response = json.loads(json.dumps(profile, indent=2))

        for key in response:
            pillar = None
            if key == "needs" or key == "values" or key == "personality":
                try:
                    pillar = Pillar.objects.get(pillar_id=key)
                except:
                    pillar = Pillar.objects.create(name=str(key).capitalize(), pillar_id=key)
                for i in range(len(response[key])):
                    if 'children' in response[key][i]:
                        category = Category.objects.create(
                            pillar=pillar,
                            name=response[key][i]["name"].encode().decode("utf-8"),
                            category=response[key][i]["category"],
                            significant=response[key][i]["significant"],
                            trait_id=response[key][i]["trait_id"]
                        )

                        category.save()

                        for j in range(len(response[key][i]["children"])):
                            subcategory = SubCategory.objects.create(
                                category=category,
                                name=response[key][i]["children"][j]["name"].encode().decode("utf-8"),
                                significant=response[key][i]["children"][j]["significant"],
                                trait_id=response[key][i]["children"][j]["trait_id"]
                            )

                            subcategory.save()
                    else:
                        category = Category.objects.create(
                            pillar=pillar,
                            name=response[key][i]["name"].encode().decode("utf-8"),
                            category=response[key][i]["category"],
                            significant=response[key][i]["significant"],
                            trait_id=response[key][i]["trait_id"]
                        )

                        category.save()
    return JsonResponse(response)

def chartsSummaries(request,pk_user):
    Usuario_filter = Persona.objects.get(pk = pk_user)
    template_name = "charts.html"
    print("en chartsSummaries")
    print("usuario entregado: "+Usuario_filter.Nombre)
    getResultSummary(request,prueba(request,Usuario_filter.Twitter),pk_user)
    data = {}

    categories = Category.objects.all()
    summaries = Summary.objects.filter(user = Usuario_filter.Usuario)
    # summaries = Summary.objects.all()

    i = 0
    dataset = []
    resultData = []
    for summary in summaries:
        if i == 0:
            dataset.append({'label': str(summary.date), 'backgroundColor': 'rgba(26,179,148,0.2)', 'borderColor': 'rgba(26,179,148,1)'})
        else:
            dataset.append({'label': str(summary.date), 'backgroundColor': 'rgba(120,120,120,0.2)', 'borderColor': 'rgba(120,120,120,1)'})
        for category in categories:
            for result in summary.categoryresult_set.filter(category = category):
                resultData.append(int(float(result.percentile)*100))
        dataset[i]["data"] = resultData
        resultData = []
        i += 1

    data["labels"] = list(Category.objects.all().values_list("name", flat = True))
    data["dataset"] = json.dumps(dataset)

    return render(request, template_name, data)
def getResultSummary(request,descripcion,pk_user):
    description = descripcion  # User text for analysis
    html = "<div>jejej una pruebilla</div>"

    profile = get_personality(description)
    response = json.loads(json.dumps(profile, indent=2))

    userProfile = User.objects.get(pk=pk_user)

    summary = Summary(
        user=userProfile,
        description=html,
        word_count=response["word_count"],
        date=datetime.now(),
        processed_language=response["processed_language"],
        json_response=json.dumps(response, ensure_ascii=False)
    )

    summary.save()

    for key in response:
        if key == "needs" or key == "values" or key == "personality":
            for dataCategory in range(len(response[key])):
                category = Category.objects.get(trait_id=response[key][dataCategory]['trait_id'])
                if 'children' in response[key][dataCategory]:
                    categoryResult = CategoryResult.objects.create(
                        summary=summary,
                        category=category,
                        percentile=response[key][dataCategory]['percentile'],
                        raw_score=response[key][dataCategory]['raw_score']
                    )

                    categoryResult.save()

                    for dataChildren in range(len(response[key][dataCategory]['children'])):
                        subCategory = SubCategory.objects.get(
                            trait_id=response[key][dataCategory]['children'][dataChildren]['trait_id'])

                        subCategoryResult = SubCategoryResult.objects.create(
                            summary=summary,
                            subcategory=subCategory,
                            percentile=response[key][dataCategory]['children'][dataChildren]['percentile'],
                            raw_score=response[key][dataCategory]['children'][dataChildren]['raw_score']
                        )

                        subCategoryResult.save()

                else:
                    categoryResult = CategoryResult.objects.create(
                        summary=summary,
                        category=category,
                        percentile=response[key][dataCategory]['percentile'],
                        raw_score=response[key][dataCategory]['raw_score']
                    )

                    categoryResult.save()

    return JsonResponse(response)
# SENTIMIENTO
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
