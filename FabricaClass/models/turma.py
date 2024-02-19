from django.db import models
from FabricaClass.models import Curso

class Turma(models.Model):
    class ano_letivo(models.IntegerChoices):
        PRIMEIROANO = (1, '1º Ano',)
        SEGUNDOANO = (2, '2º Ano',)
        TERCEIROANO = (3, '3º Ano',)

    class semestre_letivo(models.IntegerChoices):
        PRIMEIROSEMESTRE = (4, '1º Semestre',)
        SEGUNDOSEMESTRE = (5, '2º Semestre',)
        TERCEIROSEMESTRE = (6, '3º Semestre',)
        QUARTOSEMESTRE = (7, '4º Semestre',)
        QUINTOSEMESTRE = (8, '5º Semestre',)
        SEXTOSEMESTRE = (9, '6º Semestre',)
        SETIMOSEMESTRE = (10, '7º Semestre',)
        OITAVOSEMESTRE = (11, '8º Semestre',)
        NONOSEMESTRE = (12, '9º Semestre',)
        DECIMOSEMESTRE = (13, '10º Semestre',)

    legenda = models.CharField(max_length=10, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='Curso')
    ano_letivo = models.IntegerField(choices=ano_letivo.choices,  default=ano_letivo.PRIMEIROANO, blank=True, null=True)
    semestre_letivo = models.IntegerField(choices=semestre_letivo.choices,  default=semestre_letivo.PRIMEIROSEMESTRE, blank=True, null=True)

    def __str__(self):
        return self.legenda

    def save(self, *args, **kwargs):
        if (self.ano_letivo is None and self.semestre_letivo is None):
            raise ValueError("O ano ou o semestre letivo devem ser preenchidos")
        super(Turma, self).save(*args, **kwargs)