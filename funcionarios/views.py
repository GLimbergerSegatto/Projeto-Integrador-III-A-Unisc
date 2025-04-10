from django.shortcuts import render
from django.http import HttpResponse
from .forms import FuncionarioLogin, FuncionarioCadastro
from .models import Funcionario
from django.contrib.auth import authenticate, login

def funcionario_login(request):
    funcio_l = FuncionarioLogin()

    if request.method == "GET":
        return render(request, 'funcionario_login.html', {'funcio_l': funcio_l})
    else:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        autenticacao = authenticate(username=usuario, password=senha)

        if autenticacao:
            login(request, autenticacao)
            return HttpResponse("Autenticado")
        else:
            return HttpResponse("usuario ou senha invalido")


def funcionario_cadastro(request):
    funcio_c = FuncionarioCadastro()

    if request.method == "GET":
        return render(request, 'funcionario_cadastro.html', {'funcio_c': funcio_c})
    else:
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        existencia_user = Funcionario.objects.get(username=usuario)

        if existencia_user:
            return HttpResponse("Usuario ou email já existem no cadastro")
        else:
            cadastro = FuncionarioCadastro(request.POST)
            cadastro.save()

def funcionario_cadastrado(request):
    if request.method == "POST":
        cadastro = FuncionarioCadastro(request.POST)

        if cadastro.is_valid():
            funcionario = cadastro.save(commit=False)
            funcionario.set_password(cadastro.cleaned_data['password'])
            funcionario.save()
            return render(request, 'funcionario_cadastrado.html')
        else:
            return HttpResponse("Erro interno do sistema...")