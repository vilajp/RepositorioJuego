from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from apps.partida.models import Pregunta, Respuesta, Categoria

@staff_member_required
def admin(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        context = dict()
        context['categorias']= categorias
        context['mensaje']= ""

        return render(request, 'administrador.html', context)

    elif request.method == 'POST':
        
        pregunta = request.POST.get('pregunta')
        categoria , categoria_id = request.POST.get('categoria').split('_')
        respuestas = request.POST.getlist('respuesta')

        objeto_categoria = Categoria.objects.get(id = int(categoria_id))
        nueva_pregunta = Pregunta(texto = pregunta, categoria = objeto_categoria)
        
        
        alguna_correcta = False

        print(respuestas)
        respuestas = respuestas[0].split("\r\n")
        todas_las_nuevas_respuestas = list()

        for cada_respuesta in respuestas:

            print(cada_respuesta)
            if cada_respuesta[0]=="*":
                alguna_correcta = True
                nueva_respuesta = Respuesta(texto =cada_respuesta[1:], es_correcta =True, pregunta = nueva_pregunta)
                todas_las_nuevas_respuestas.append(nueva_respuesta)
            else:
                nueva_respuesta = Respuesta(texto =cada_respuesta, es_correcta =False, pregunta = nueva_pregunta)
                todas_las_nuevas_respuestas.append(nueva_respuesta)
        if alguna_correcta:
            nueva_pregunta.save()
            for cada_respuesta_nueva in todas_las_nuevas_respuestas:
                cada_respuesta_nueva.save()

        return redirect('administrador')





