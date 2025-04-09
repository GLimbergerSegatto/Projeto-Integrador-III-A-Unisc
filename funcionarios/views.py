from django.shortcuts import render
from django.http import HttpResponse
from .forms import FuncionarioLogin, FuncionarioCadastro

def funcionario_login(request):
    funcio_l = FuncionarioLogin()
    return render(request, 'funcionario_login.html', {'funcio_l': funcio_l})

def funcionario_cadastro(request):
    funcio_c = FuncionarioCadastro()
    return render(request, 'funcionario_cadastro.html', {'funcio_c': funcio_c})

def funcionario_cadastrado(request):
    cadastro = FuncionarioCadastro(request.POST)

    if cadastro.is_valid():
        cadastro.save()
        return render(request, 'funcionario_cadastrado.html')
    else:
        return HttpResponse("Erro interno do sistema...")