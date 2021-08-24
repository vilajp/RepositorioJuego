from apps.partida.models import Respuesta, Pregunta, Categoria
#pip install django-extensions
#agregar:INSTALLED_APPS [django-extensions,]
#usar: python manage.py runscript -v3 copio_preguntas


def es_digito(string):
    if string in [str(x) for x in range(10)]:
        return True
    else:
        return False

def es_respuesta(string):
    for separador in [".", ")"]:
        if string in [x+separador for x in "abcdefghijklmnñopqrstuvwxyzs"]:
            return True
    return False

archivo_preguntas = open('preguntas.txt','r')

#genero diccionario desde archivo txt

dic_preguntas = dict()

for cada_linea in archivo_preguntas.readlines():
    
    if es_digito(cada_linea[0]):
        categoria_texto = cada_linea.strip()
        dic_preguntas[categoria_texto] = dict()
        es_pregunta = True
        
    elif es_pregunta and cada_linea.strip() and not es_respuesta(cada_linea[0:2]):
        pregunta = cada_linea.strip()
        dic_preguntas[categoria_texto][pregunta] = list()
        
    elif es_respuesta(cada_linea[0:2]) and cada_linea.strip():
        dic_preguntas[categoria_texto][pregunta].append(cada_linea.strip())

print(dic_preguntas)
    
#recorro el diccionario


for categoria, pregunta in dic_preguntas.items():
    print(f"{categoria}") 
    todas_las_categorias = Categoria(nombre = categoria[2:].strip())
    todas_las_categorias.save()
    for cada_pregunta, respuestas in pregunta.items():
        print(f"{cada_pregunta}")
        todas_las_preguntas = Pregunta(texto = cada_pregunta, categoria = todas_las_categorias)
        todas_las_preguntas.save()
        for cada_respuesta in respuestas:
            print(f"{cada_respuesta}")
            if cada_respuesta[-1]=="c":
                todas_las_respuestas = Respuesta(texto =cada_respuesta[2:-3].strip(), es_correcta =True, pregunta = todas_las_preguntas)
            else:
                todas_las_respuestas = Respuesta(texto =cada_respuesta[2:].strip(), es_correcta =False, pregunta = todas_las_preguntas)
            
            todas_las_respuestas.save()

    