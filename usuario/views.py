from rest_framework.viewsets import ModelViewSet
from .models import Usuario, Professor, Aluno
from .serializers import UsuarioSerializer, AlunoSerializer, ProfessorSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = UsuarioSerializer
class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = UsuarioSerializer    