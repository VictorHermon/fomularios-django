from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    contexto = {
        'form': PassagemForms()
    }
    return render(request, 'index.html', contexto)
