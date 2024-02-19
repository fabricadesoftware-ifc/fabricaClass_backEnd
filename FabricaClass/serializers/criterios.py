from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Criterios

class CriteriosSerializer(ModelSerializer):
    class Meta:
        model = Criterios
        fields = "__all__"