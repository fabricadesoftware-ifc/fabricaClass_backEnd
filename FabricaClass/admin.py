from django.contrib import admin
from .models import Curso, Turma, Formulario, Respostas, Criterios, Pergunta

# Register your models here.
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Formulario)
admin.site.register(Respostas)
admin.site.register(Criterios)
admin.site.register(Pergunta)