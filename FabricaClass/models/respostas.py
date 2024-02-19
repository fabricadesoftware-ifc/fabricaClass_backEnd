from django.db import models
from FabricaClass.models import Formulario

class Respostas(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    resposta = models.CharField(max_length=255)
    formulario = models.ForeignKey(Formulario, on_delete=models.PROTECT, related_name='formulario')
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.resposta