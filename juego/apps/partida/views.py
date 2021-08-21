from django.shortcuts import render, redirect

from apps.partida.models import Pregunta, RespuestaCorrecta, RespuestaIncorrecta
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
        
        respuesta, id_pregunta = request.POST.get("respuesta").split("_")
        una_respuesta = RespuestaCorrecta.objects.get(pregunta_id = id_pregunta)
        pregunta = Pregunta.objects.get(id = id_pregunta)
        u = Usuario.objects.get(username=str(request.user))

        u.pregunta_contestada.add(pregunta)
        print(pregunta)
        print(u.pregunta_contestada)

        if respuesta == str(una_respuesta):
            u.puntaje +=10

        u.save()   
            


        return redirect('partida')

@login_required
def home(request):
    return render(request, 'home.html')
