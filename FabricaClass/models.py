from django.db import models

class Curso(models.Model):
    class TurnoCurso(models.IntegerChoices):
        Matutino = (1, "Matutino",)
        Vespertino = (2, "Vespertino",)
        Noturno = (3, "Noturno",)
        Integral = (4, "Integral",)
    nome = models.CharField(max_length=255, blank=True, null=True)
    turno = models.IntegerField(choices=TurnoCurso.choices,  default=TurnoCurso.Integral)
class Turma(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='curso')

