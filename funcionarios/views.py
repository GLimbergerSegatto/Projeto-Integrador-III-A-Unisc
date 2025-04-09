from django.shortcuts import render
from .forms import FuncionarioLogin, FuncionarioCadastro

def funcionario_login(request):
    funcionario_login = FuncionarioLogin()
    return render(request, 'funcionario_login.html', {'funcionario_login': funcionario_login})