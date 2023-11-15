from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializers import UsuarioSerializer, AlunoSerializer, ProfessorSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class ProfessorViewSet(ModelViewSet):
    queryset = Usuario.objects.filter(tipo_usuario=Usuario.TipoUsuario.PROFESSOR)
    serializer_class = UsuarioSerializer
class AlunoViewSet(ModelViewSet):
    queryset = Usuario.objects.filter(tipo_usuario=Usuario.TipoUsuario.ALUNO)
    serializer_class = UsuarioSerializer    