import asyncio
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

async def save_pie_graph(subject, message, recipient_list):
    try:
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        recipe = ["375 g flour",
                  "75 g sugar",
                  "240 g butter",
                  "300 g berries"]

        data = [float(x.split()[0]) for x in recipe]
        ingredients = [x.split()[-1] for x in recipe]

        def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return f"{pct:.1f}%\n({absolute:d} g)"

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))

        ax.legend(wedges, ingredients,
                  title="Ingredients",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("Matplotlib bakery: A pie")

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            imagem_temporaria = temp_file.name
            plt.savefig(imagem_temporaria)
            print(imagem_temporaria)

        remetente = "suporte.fabricaclass@gmail.com"
        senha = "hvnz resu zood wosz"

        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = ", ".join(recipient_list)
        msg['Subject'] = subject

        with open(imagem_temporaria, 'rb') as fp:
            img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename=imagem_temporaria)
        msg.attach(img)

        # Envio síncrono de e-mail usando send_mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)

        server.sendmail(remetente, recipient_list, msg.as_string())
        server.quit()

        return "Email enviado com sucesso"
    except Exception as e:
        # Em caso de exceção, retorne None ou outra indicação de falha
        print(f"Erro ao gerar imagem ou enviar e-mail: {e}")
        return None

class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.POST.get("subject", "Nome do email")
        message = request.POST.get("message", "Conteúdo do email")
        recipient_list = ["lucasantonete@hotmail.com", "fabio.moura@ifc.edu.br"]

        # Chamada assíncrona para a função
        resultado_envio = asyncio.run(save_pie_graph(subject, message, recipient_list))

        if resultado_envio:
            return HttpResponse(resultado_envio, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Erro ao enviar email", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
