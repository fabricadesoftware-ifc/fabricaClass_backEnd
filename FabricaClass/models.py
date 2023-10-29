from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=10, blank=True, null=True)
class Turma(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='curso')
