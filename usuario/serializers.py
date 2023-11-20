from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Usuario
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "TipoUsuario.PROFESSOR"
class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "TipoUsuario.ALUNO"
