from django.shortcuts import render
from .models import Funcionario
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def funcionario_login(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        login = authenticate(username=usuario, password=senha)
        
        if login is not None:
            login(request, login)
            return render(request , '') #Home entrará aqui
        
    return render(request, 'funcionario_login.html')

def funcionario_cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        genero = request.POST.get('genero')
        estado = request.POST.get('estado')
        funcao = request.POST.get('funcao')
        senha = request.POST.get('senha')

        funcionario = Funcionario.objects.create_user(
                nome=nome,
                usuario=usuario,
                email=email,
                genero=genero,
                estado=estado,
                funcao=funcao,
                senha=senha, 
            )
        
        return redirect('cadastro_sucesso')
    
    return render(request, 'funcionario_cadastro.html')

def cadastro_sucesso(request):
    return render(request, 'cadastro_sucesso.html')