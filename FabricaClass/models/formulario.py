from django.db import models
from .pergunta import Pergunta
import datetime

class Formulario(models.Model):
    data_hora_limite = datetime
    data_inicio = datetime.datetime.now()
    data_fim = datetime
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
