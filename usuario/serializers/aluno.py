from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "TipoUsuario.ALUNO"
