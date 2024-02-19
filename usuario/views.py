from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from .serializer import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer