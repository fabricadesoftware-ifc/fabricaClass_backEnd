from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Usuario, Professor, Aluno
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"
class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"  
