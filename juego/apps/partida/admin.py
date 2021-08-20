from django.contrib import admin
from .models import Pregunta, RespuestaCorrecta, RespuestaIncorrecta


# Register your models here.
admin.site.register(Pregunta)
admin.site.register(RespuestaCorrecta)
admin.site.register(RespuestaIncorrecta)
