from django.shortcuts import render, redirect

from apps.partida.models import Pregunta, Respuesta, PreguntaContestada
from apps.usuarios.models import Usuario
import random
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
#Esta funcion carga una pregunta aleatoria
@login_required
def comienzo(request):

    if request.method == 'GET':
        respuestas = list()

        lista_preguntas = Pregunta.objects.all()
        cantidad = len(lista_preguntas)
        una_id = random.randint(1,cantidad)
        una_pregunta = Pregunta.objects.get(id=una_id)
        # Se obtienen las respuestas
        for r in Respuesta.objects.all():
            if r.pregunta_id == una_pregunta.pk:
                respuestas.append(r)

        context = {"pregunta":una_pregunta,"respuestas":respuestas}
        return render(request,"partida.html",context)

    elif request.method == 'POST':
        return HttpResponse('RESTAURAR POST, está comentado en view porque hay que adaptarlo')
        # respuesta, id_pregunta = request.POST.get("respuesta").split("_")
        # una_respuesta = RespuestaCorrecta.objects.get(pregunta_id = id_pregunta)
        #
        # p = Pregunta.objects.get(id = id_pregunta)
        # u = Usuario.objects.get(username=str(request.user))
        #
        # if respuesta == str(una_respuesta):
        #     u.puntaje +=10
        #
        # u.save()
        # PreguntaContestada(usuario=u, pregunta=p).save()
        # return redirect('partida')

@login_required
def home(request):
    return render(request, 'home.html')
