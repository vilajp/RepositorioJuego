from django.contrib import admin
from .models import Preguntas,Respuestas,Respuesta_Incorrecta


# Register your models here.
admin.site.register(Preguntas)
admin.site.register(Respuestas)
admin.site.register(Respuesta_Incorrecta)