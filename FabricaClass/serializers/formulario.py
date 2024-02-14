from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Formulario

class FormularioSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields = "__all__"