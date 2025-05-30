from django.urls import path
from . import views

#Diretórios das funções views que apresentam as páginas
urlpatterns = [
    path('funcionario_login/', views.funcionario_login, name="funcionario_login"),
    path('funcionario_cadastro/', views.funcionario_cadastro, name="funcionario_cadastro"),
    path('cadastro_sucesso/', views.cadastro_sucesso, name="cadastro_sucesso"),
]