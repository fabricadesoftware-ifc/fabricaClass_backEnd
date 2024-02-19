from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Formulario
from FabricaClass.serializers import FormularioSerializer

class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer