from django.shortcuts import render
from apps.partida.models import Juego
from apps.usuarios.models import Usuario
# Create your views here.

def estadistica(request):
    j = Juego.objects.all()
    u = Usuario.objects.all()
    acumulador_preguntas = 0
    acumulador_puntaje = 0
    dic_jugadas = dict()
    dic_jugadas['usuario']=dict()
    efectividad = 0
    for cada_usuario in u:

        for cada_jugada in j:
            if cada_usuario.id == cada_jugada.usuario_id:
                acumulador_preguntas += cada_jugada.cantidad_preguntas_contestadas
                acumulador_puntaje += cada_jugada.puntaje

            if acumulador_preguntas != 0:
                efectividad = ((acumulador_puntaje/10)/acumulador_preguntas)*100

            dic_jugadas['usuario'][cada_usuario.username] = [acumulador_preguntas, acumulador_puntaje,efectividad]
        print(dic_jugadas)
        acumulador_preguntas = 0
        acumulador_puntaje = 0
        efectividad = 0

    #ordenamos el diccionario
    dic_ordenado = dict()
    dic_ordenado['usuario'] = dict()
    puntaje_mayor = 0
    while len(dic_jugadas['usuario']) > 0:

        for k, v in dic_jugadas['usuario'].items():
            print(k,v)
            if v[1] >= puntaje_mayor:
                usuario_mayor = k
                preguntas = v[0]
                puntaje_mayor = v[1]
                efectividad = v[2]
        dic_ordenado['usuario'][usuario_mayor] = [preguntas, puntaje_mayor, efectividad]
        del dic_jugadas['usuario'][usuario_mayor]
        puntaje_mayor = 0
    print(dic_ordenado)

    return render(request, 'estadistica.html', dic_ordenado)
