from django import forms
from .models import Funcionario

#Login: usuário, senha
class FuncionarioLogin(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['username', 'password']
        
        labels = {
            'username': 'Usuário',
            'password': 'Senha',
        }

        widgets = {
            'password': forms.PasswordInput(),
        }

#Cadastro: todos os fields para preencher
class FuncionarioCadastro(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'username', 'email', 'genero', 'estado', 'funcao', 'password']
        
        labels = {
            'username': 'Usuário',
            'password': 'Senha',
            'email': 'E-Mail',
            'nome': 'Nome',
            'genero': 'Gênero',
            'funcao': 'Função',
            'estado': 'Estado',
        }

        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }