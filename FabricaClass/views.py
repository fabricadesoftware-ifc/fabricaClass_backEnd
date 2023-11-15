from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings

class SendEmailView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [request.data.get('recipient_email')]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        return Response({"message": "E-mail enviado com sucesso!"}, status=status.HTTP_200_OK)

