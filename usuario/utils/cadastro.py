from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from usuario.models import Usuario
from rest_framework.response import Response
from rest_framework import status
from ..models import Usuario
from django.contrib.auth import get_user_model
User = get_user_model()

@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def create_user(request):
    email = request.data.get("email")
    password = request.data.get("password")
    telefone = request.data.get("telefone")
    username = request.data.get("username")
    tipo_usuario = request.data.get("tipo_usuario")
    matricula = request.data.get("matricula")

    if Usuario.objects.filter(email=email).exists():
        return Response({"error": "Email já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)
    if email and password:
        user = Usuario.objects.create(
            email=email,
            telefone=telefone,
            username=username,
            tipo_usuario=tipo_usuario,
            matricula=matricula
        )
        user.set_password(password)
        user.save()
        return Response({"success": "Usuário criado com sucesso"}, status=status.HTTP_201_CREATED)