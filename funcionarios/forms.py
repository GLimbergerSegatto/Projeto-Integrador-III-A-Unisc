from django import forms
from .models import Funcionario

#Login: usuário, senha
class FuncionarioLogin(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['usuario', 'senha']
        
        labels = {
            'usuario': 'Usuário',
            'senha': 'Senha',
        }

        widgets = {
            'senha': forms.PasswordInput(),
        }

#Cadastro: todos os fields para preencher
class FuncionarioCadastro(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'usuario', 'genero', 'estado', 'funcao', 'senha']
        
        labels = {
            'usuario': 'Usuário',
            'senha': 'Senha',
            'nome': 'Nome',
            'genero': 'Gênero',
            'funcao': 'Função',
            'estado': 'Estado',
        }

        widgets = {
            'senha': forms.PasswordInput(),
        }