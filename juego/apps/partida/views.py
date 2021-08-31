from django.shortcuts import render, redirect
import math

from apps.partida.models import Pregunta, Respuesta, PreguntaContestada, Juego, Categoria
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
        u = Usuario.objects.get(username=str(request.user))
        
        pc = PreguntaContestada.objects.filter(usuario = u.id)

        lista_pc = [x.pregunta_id for x in pc]
      

        j = Juego.objects.latest('id')

        puntaje = j.puntaje
        lista_preguntas = Pregunta.objects.all()
        cantidad = len(lista_preguntas)
        
        if len(lista_pc)>0:
            numero = int(puntaje)/100
            nivel = str(math.floor(numero)+1)
        else:
            nivel = "1"


        mensaje = ""

        while cantidad > len(lista_pc):
            una_id = random.randint(1,cantidad)

            if una_id not in lista_pc:
                una_pregunta = Pregunta.objects.get(id=una_id)
                categoria_pregunta = Categoria.objects.get(id = una_pregunta.categoria.pk)
                break
        else:
            mensaje = "Ya termino de contestar todas las preguntas"

        # Se obtienen las respuestas
        for r in Respuesta.objects.all():
            if r.pregunta_id == una_pregunta.pk:
                respuestas.append(r)

        context = {"pregunta":una_pregunta,
                "respuestas":respuestas, 
                "puntaje":puntaje,
                "mensaje":mensaje, 
                "categoria":categoria_pregunta.nombre,
                "nivel":nivel}

        return render(request,"partida.html",context)

    elif request.method == 'POST':

        lista_respuestas = list()
        try:
            for cada_respuesta in request.POST.getlist('respuesta'):
                una_respuesta_id, id_pregunta = cada_respuesta.split("_")
                lista_respuestas.append(int(una_respuesta_id))

            respuestas_correctas = Respuesta.objects.all().filter(pregunta = id_pregunta, es_correcta=1)
            lista_correctas = [x.id for x in respuestas_correctas]

            lista_correctas.sort()
            lista_respuestas.sort()

            u = Usuario.objects.get(username=str(request.user))
            j = Juego.objects.latest('id')
            j.cantidad_preguntas_contestadas += 1

            p = Pregunta.objects.get(id = id_pregunta)
            
            if lista_correctas == lista_respuestas:

                j.puntaje +=10
                j.usuario = u
                pc= PreguntaContestada(usuario=u, pregunta=p, correcta=True)

            else:

                pc= PreguntaContestada(usuario=u, pregunta=p)
            
            j.save()
            pc.save()
            
            
            
        except:
            print("No se cargo una pregunta")
        finally:
            return redirect('partida')



        print(lista_correctas)
        print(lista_respuestas)



        # respuesta, id_pregunta = request.POST.get("respuesta").split("_")
        # una_respuesta = RespuestaCorrecta.objects.get(pregunta_id = id_pregunta)
        #
        #
        # return redirect('partida')

@login_required
def home(request):
    return render(request, 'home.html')

def creo_juego(request):
    j = Juego.objects.filter(usuario = request.user)


    j = Juego(usuario=request.user)
    j.save()
    return redirect('partida')

@login_required
def borrar(request):

    u = Usuario.objects.get(username=str(request.user))

    PreguntaContestada.objects.filter(usuario_id=u.id).delete()

    return redirect('creo-juego')
