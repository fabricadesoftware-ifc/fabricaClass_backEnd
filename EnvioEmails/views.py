from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject', '')
        message = request.data.get('message', '')
        recipient_list = request.data.get('recipient_list', '')

        try:
            send_mail(subject, message, 'suporte.fabricaclass@gmail.com', recipient_list, fail_silently=False)
            return Response({'message': 'Email enviado com sucesso'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    