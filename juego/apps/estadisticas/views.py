from django.shortcuts import render
from apps.partida.models import Juego
from apps.usuarios.models import Usuario
# Create your views here.

def estadistica(request):
    j = Juego.objects.all()
    u = Usuario.objects.all()
    acumulador = 0
    acumulador_puntaje = 0
    dic_jugadas = dict()
    dic_jugadas['usuario']=dict()
    for cada_usuario in u:
        
        for cada_jugada in j:
            if cada_usuario.id == cada_jugada.usuario_id:
                acumulador  += cada_jugada.cantidad_preguntas_contestadas
                acumulador_puntaje += cada_jugada.puntaje


        dic_jugadas['usuario'][cada_usuario.username] = [acumulador, acumulador_puntaje]
        acumulador = 0
        acumulador_puntaje = 0
    dic_ordenado = dict()
    dic_ordenado['usuario'] = dict()
    mayor = 0
    while len(dic_jugadas['usuario']) > 0:
        for k, v in dic_jugadas['usuario'].items():
            if v[1] > mayor:
                preguntas = v[0]
                puntaje_mayor = v[1]
        dic_ordenado['usuario'][k] = [preguntas, puntaje_mayor]
        del dic_jugadas['usuario'][k]    

    print(dic_jugadas)   
    return render(request, 'estadistica.html', dic_ordenado)

