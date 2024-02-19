from django.db import models

class Curso(models.Model):

    class TipoCurso(models.IntegerChoices):
        Graduacao = (1, "Graduação",)
        Tecnico = (2, "Técnico",)
        
    class NomeCurso(models.IntegerChoices):
        Informatica = (1, "Informática",)
        MedicinaVeterinaria = (2, "Medicina Veterinária",)

    class TurnoCurso(models.IntegerChoices):
        Matutino = (1, "Matutino",)
        Vespertino = (2, "Vespertino",)
        Noturno = (3, "Noturno",)
        Integral = (4, "Integral",)
    nome = models.CharField(max_length=255, blank=True, null=True)
    turno = models.IntegerField(choices=TurnoCurso.choices,  default=TurnoCurso.Integral)

    def __str__(self):
        return self.nome