from django.contrib import admin
from .models import Pregunta, Respuesta, Categoria


# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Categoria)
