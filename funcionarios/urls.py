from django.urls import path
from . import views

urlpatterns = [
    path('funcionario_login/', views.funcionario_login, name="funcionario_login")
]