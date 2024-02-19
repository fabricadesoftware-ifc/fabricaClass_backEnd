from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Respostas

class RespostasSerializer(ModelSerializer):
    class Meta:
        model = Respostas
        fields = "__all__"