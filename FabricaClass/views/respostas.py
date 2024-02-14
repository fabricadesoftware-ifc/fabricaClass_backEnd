from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Respostas
from FabricaClass.serializers import RespostasSerializer

class RespostasViewSet(ModelViewSet):
    queryset = Respostas.objects.all()
    serializer_class = RespostasSerializer