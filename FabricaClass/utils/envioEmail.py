#from rest_framework.views import APIView
#from rest_framework import status
#from django.core.mail import BadHeaderError, send_mail
#from django.http import HttpResponse


#class EmailAPIView(APIView):
#    def post(self, request, *args, **kwargs):
#        subject = request.POST.get("subject", "Nome do email")
#        message = request.POST.get("message", "Conteúdo do email")
#        imagem_temporaria = request.FILES.get(save_pie_graph[imagem_temporaria])
#        recipient_list = ["lucasantonete@hotmail.com", "fabio.moura@ifc.edu.br"]
#        from_email = "suporte.fabricaclass@gmail.com"
        
#        if imagem_temporaria is not None:
#            try:
                # Envio síncrono de e-mail usando send_mail
#                send_mail(
#                    subject,
#                    message,
#                    from_email,
#                    recipient_list,
#                    attachments=[(imagem_temporaria, 'image/png')],
#                )
#            except BadHeaderError:
#                return HttpResponse("Invalid header found.", status=status.HTTP_400_BAD_REQUEST)
#            except Exception as e:
#                return HttpResponse(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
#            return HttpResponse("Email enviado com sucesso", status=status.HTTP_200_OK)
#        else:
#           return HttpResponse("Imagem temporária não encontrada", status=status.HTTP_400_BAD_REQUEST)
