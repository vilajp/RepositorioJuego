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
        respuestas = request.POST.getlist('respuestas')

        objeto_categoria = Categoria.objects.get(id = int(categoria_id))
        nueva_pregunta = Pregunta(texto = pregunta, categoria = objeto_categoria)
        
        
        alguna_correcta = False
        for cada_respuesta in respuestas:

            print(cada_respuesta)
            if cada_respuesta[0].strip("\r\n")=="*":
                alguna_correcta = True
                nueva_respuesta = Respuesta(texto =cada_respuesta[1:].strip("\r\n"), es_correcta =True, pregunta = nueva_pregunta)
            else:
                nueva_respuesta = Respuesta(texto =cada_respuesta.strip("\r\n"), es_correcta =False, pregunta = nueva_pregunta)

        if alguna_correcta:
            nueva_pregunta.save()
            nueva_respuesta.save()

        return redirect('administrador')




