from django.shortcuts import render
from apps.partida.models import Preguntas,Respuestas, Respuesta_Incorrecta
import random
# Create your views here.
#Esta funcion carga una pregunta aleatoria
def comienzo(request):
    lista_preguntas = Preguntas.objects.all()
    cantidad = len(lista_preguntas)
    una_id = random.randint(1,cantidad)
    una_pregunta = Preguntas.objects.get(id=una_id)
    if request.method == 'GET':
        context = {"pregunta":una_pregunta,"respuesta":una_pregunta.respuesta_correcta,"incorrecta":una_pregunta.respuesta_erronea}
        return render(request,"partida.html",context)

    elif request.method == 'POST':
        if request.POST.get("respuesta") == str(una_pregunta.respuesta_correcta):
            return HttpResponse("Felicidades!!!")
        else:
            return HttpResponse("Fallaste!!!")

    

def home(request):
    return render(request, 'home.html')

