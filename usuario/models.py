from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from FabricaClass.models import Curso, Turma
from django.contrib.auth.models import Group, Permission

from .managers import CustomUserManager


class Usuario(AbstractUser):
    #username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    username = models.CharField(_("Nome"), max_length=255, blank=True, null=True)
    #cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    #telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    #data_nascimento = models.DateField(
    #    _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    #)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]

class Professor(models.Model): 
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='professor')
    siape = models.CharField(_("SIMPE"), max_length=11, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='professor_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='professor_user_permissions')


class Aluno(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='aluno')
    matricula = models.CharField(_("Matricula"), max_length=11, blank=True, null=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    id_turma = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name='turma', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='aluno_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='aluno_user_permissions')
    class  ano_letivo(models.IntegerChoices):
        PRIMEIRO = 1, _('Primeiro')
        SEGUNDO = 2, _('Segundo')
        TERCEIRO = 3, _('Terceiro')
        
                                 