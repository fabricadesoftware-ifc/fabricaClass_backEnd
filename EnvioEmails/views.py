from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ValidationError
from django.http import HttpResponse
class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.POST.get("subject", "teste")
        print(subject)
        message = request.POST.get("message", "testando")
        recipient_list = ["lucasantonete@hotmail.com", "suporte.fabricaclass@gmail.com"]

        try:
            send_mail(
                subject,
                message,
                recipient_list=recipient_list,
                from_email="suporte.fabricaclass@gmail.com",
                 )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except ValidationError as e:
            return HttpResponse(str(e))
        return HttpResponse(
            {"message": "Email enviado com sucesso"}, status=status.HTTP_200_OK
        )