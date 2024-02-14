from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Turma

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = "__all__"