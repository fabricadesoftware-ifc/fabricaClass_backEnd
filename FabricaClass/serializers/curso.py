from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Curso

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"