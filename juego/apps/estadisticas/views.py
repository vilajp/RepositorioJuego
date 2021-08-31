from django.shortcuts import render
from apps.partida.models import Juego, PreguntaContestada, Pregunta, Respuesta
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
                acumulador_puntaje += int(cada_jugada.puntaje/10)

            if acumulador_preguntas != 0:
                efectividad = int(((acumulador_puntaje)/acumulador_preguntas)*100)

            total_puntaje = acumulador_puntaje *10
            dic_jugadas['usuario'][cada_usuario.username] = [acumulador_preguntas, acumulador_puntaje,efectividad, total_puntaje]
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
                total_puntaje = v[3]
        dic_ordenado['usuario'][usuario_mayor] = [preguntas, puntaje_mayor, efectividad, total_puntaje]
        del dic_jugadas['usuario'][usuario_mayor]
        puntaje_mayor = 0
    print(dic_ordenado)

    return render(request, 'estadistica.html', dic_ordenado)

def resultados_juego(request):
    
    u = Usuario.objects.get(username=str(request.user))
    preguntas_contestadas = PreguntaContestada.objects.filter(usuario_id=u.id)


    preguntas_correctas = PreguntaContestada.objects.filter(correcta=True, usuario_id=u.id)

    
    
    informe_juego= dict()
    informe_juego['resultados']= dict()
    informe_juego['cantidad']= len(preguntas_contestadas)
    informe_juego['correctas'] = len(preguntas_correctas)


    for cada_pregunta_contestada in preguntas_contestadas:

        respuestas_correctas = Respuesta.objects.filter(pregunta_id = cada_pregunta_contestada.pregunta_id, es_correcta =True)

        print(respuestas_correctas)

        una_pregunta = Pregunta.objects.get(id = cada_pregunta_contestada.pregunta_id)

        informe_juego['resultados'][una_pregunta.texto]=list()

        textos_respuestas_correctas = [x.texto for x in respuestas_correctas]
        
        print(textos_respuestas_correctas)


        if cada_pregunta_contestada.correcta:

            informe_juego['resultados'][una_pregunta.texto].append("correcta")
            
        else:
            
            informe_juego['resultados'][una_pregunta.texto].append("incorrecta")
            
        informe_juego['resultados'][una_pregunta.texto].append(textos_respuestas_correctas)
    context = informe_juego

    return render(request, "resultados.html", context)


            



