from django.shortcuts import render
from apps.partida.models import Pregunta, RespuestaCorrecta, RespuestaIncorrecta
import random
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
#Esta funcion carga una pregunta aleatoria
def comienzo(request):
    if request.method == 'GET':
        respuestas = list()

        lista_preguntas = Pregunta.objects.all()
        cantidad = len(lista_preguntas)
        una_id = random.randint(1,cantidad)
        una_pregunta = Pregunta.objects.get(id=una_id)
        # Se obtiene la respuesta correcta
        for rc in RespuestaCorrecta.objects.all():
            if rc.pregunta_id == una_pregunta.pk:
                respuestas.append(rc)
                break
        # Se obtiene las respuestas incorrectas
        for ri in RespuestaIncorrecta.objects.all():
            if ri.pregunta_id == una_pregunta.pk:
                respuestas.append(ri)

        context = {"pregunta":una_pregunta,"respuestas":respuestas}
        return render(request,"partida.html",context)
    elif request.method == 'POST':
        #print(request)
        return HttpResponse(request)

@login_required
def home(request):
    return render(request, 'home.html')
