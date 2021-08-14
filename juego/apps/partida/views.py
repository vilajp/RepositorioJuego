from django.shortcuts import render
from apps.partida.models import Preguntas,Respuestas
import random
# Create your views here.

def comienzo(request):
    lista_preguntas = Preguntas.objects.all()
    cantidad = len(lista_preguntas)
    una_id = random.randint(1,cantidad)
    una_pregunta = Preguntas.objects.get(id=una_id)
    context = {"pregunta":una_pregunta}
    return render(request,"partida.html",context)

