from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms


def index(request):
    contexto = {
        'form': PassagemForms(),
        'pessoa_form': PessoaForms()
    }
    return render(request, 'index.html', contexto)


def revisao_consulta(request):
    if request.method == 'POST':
        contexto = {
            'form': PassagemForms(request.POST),
            'pessoa_form': PessoaForms(request.POST)
        }
        if contexto['form'].is_valid():
            return render(request, 'minha_consulta.html', contexto)
        else:
            return render(request, 'index.html', contexto)
