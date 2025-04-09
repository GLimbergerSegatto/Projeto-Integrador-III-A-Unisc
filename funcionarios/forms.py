from django import forms
from .models import Funcionario

class FuncionarioCadastro(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'genero', 'funcao', 'estado', 'usuario', 'senha']
        
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