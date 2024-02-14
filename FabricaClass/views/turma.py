from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import  Turma
from FabricaClass.serializers import TurmaSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer