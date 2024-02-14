from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from usuario.serializers import ProfessorSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Usuario.objects.filter(tipo_usuario=Usuario.TipoUsuario.PROFESSOR)
    serializer_class = ProfessorSerializer