from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from usuario.serializers import AlunoSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Usuario.objects.filter(tipo_usuario=Usuario.TipoUsuario.ALUNO)
    serializer_class = AlunoSerializer    