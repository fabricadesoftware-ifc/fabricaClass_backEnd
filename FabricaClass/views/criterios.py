from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Criterios
from FabricaClass.serializers import CriteriosSerializer

class CriteriosViewSet(ModelViewSet):
    queryset = Criterios.objects.all()
    serializer_class = CriteriosSerializer