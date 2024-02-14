from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Curso
from FabricaClass.serializers import CursoSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer