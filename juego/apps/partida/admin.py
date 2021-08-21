from django.contrib import admin
from .models import Pregunta, RespuestaCorrecta, RespuestaIncorrecta, Categoria


# Register your models here.
admin.site.register(Pregunta)
admin.site.register(RespuestaCorrecta)
admin.site.register(RespuestaIncorrecta)
admin.site.register(Categoria)
