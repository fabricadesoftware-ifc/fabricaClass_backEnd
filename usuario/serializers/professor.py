from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "TipoUsuario.PROFESSOR"
