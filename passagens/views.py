from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    contexto = {
        'form': PassagemForms()
    }
    return render(request, 'index.html', contexto)


def revisao_consulta(request):
    if request.method == 'POST':
        contexto = {
            'form': PassagemForms(request.POST)
        }
        if contexto['form'].is_valid():
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Formulário Inválido')
            return render(request, 'index.html', contexto)
