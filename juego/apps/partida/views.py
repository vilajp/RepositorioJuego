from django.shortcuts import render
from apps.partida.models import Preguntas,Respuestas, Respuesta_Incorrecta
import random
# Create your views here.
#Esta funcion carga una pregunta aleatoria
def comienzo(request,respuesta=""):
    if respuesta=="":
        lista_preguntas = Preguntas.objects.all()
        cantidad = len(lista_preguntas)
        una_id = random.randint(1,cantidad)
        una_pregunta = Preguntas.objects.get(id=una_id)
        context = {"pregunta":una_pregunta,"respuesta":una_pregunta.respuesta_correcta,"incorrecta":una_pregunta.respuesta_erronea}
        return render(request,"prueba.html",context)

    else:
        print(respuesta)

    

def home(request):
    return render(request, 'home.html')

