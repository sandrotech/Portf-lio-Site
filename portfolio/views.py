from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import os
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # opcional se não estiver usando {% csrf_token %}
from django.contrib import messages

@csrf_exempt
def enviar_email(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        corpo_email = (
            f"Mensagem enviada pelo site de Alessandro Santos\n\n"
            f"Nome: {nome}\n"
            f"E-mail: {email}\n"
            f"Mensagem:\n{mensagem}"
        )

        try:
            email_obj = EmailMessage(
                subject=f"[PORTFÓLIO] Contato de {nome}",
                body=corpo_email,
                from_email='sandro.santostech@gmail.com',
                to=['sandro.santostech@gmail.com'],
                reply_to=[email]
            )
            email_obj.send(fail_silently=False)
        except Exception as e:
            print("Erro ao enviar e-mail:", e)
        return redirect('home')

def home(request):
    return render(request, 'home.html')