from django.urls import path
from . import views

#Diretórios das funções views que apresentam as páginas
urlpatterns = [
    path('funcionario_login/', views.funcionario_login, name="funcionario_login"),
    path('funcionario_cadastro/', views.funcionario_cadastro, name="funcionario_cadastro"),
    path('funcionario_cadastrado/', views.funcionario_cadastrado, name="funcionario_cadastrado"),
]