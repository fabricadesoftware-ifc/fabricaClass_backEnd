from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Pergunta
from FabricaClass.serializers import PerguntaSerializer

class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer