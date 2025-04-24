from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#Gerenciador da da tabela funcionario
class FuncionarioManager(BaseUserManager):
    def create_user(self, nome, genero, funcao, estado, usuario, senha, email):
        if not email:
            raise ValueError("Digite o campo de email corretamente")
        if not usuario:
            raise ValueError("Digite o campo de usuário corretamente")
        
        user = self.model(
            nome = nome,
            genero = genero,
            funcao = funcao,
            estado = estado,
            usuario = usuario,
            email = self.normalize_email(email) 
        )

        user.set_password(senha)
        user.save(using = self._db)
        return user

#Tabela funcionario
class Funcionario(AbstractBaseUser, PermissionsMixin):

    objects = FuncionarioManager()

    #Aqui estão algumas opções para campos enumerados na tabela funcionario
    generos = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    funcoes = [
        ('ACG', 'Açougueiro'),
        ('LIM', 'Encarregado de limpeza'),
        ('REP', 'Repositor'),
        ('CAX', 'Operador do Caixa'),
        ('EMP', 'Empacotador'),
        ('ADM', 'Administrador'),
        ('PAD', 'Padeiro'),
    ]
    
    estados = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    
    #Aqui estão as colunas da tabela funcionario
    nome = models.CharField(max_length=100, null=False, blank=False)
    genero = models.CharField(max_length=1, choices=generos, null=False, blank=False)
    funcao = models.CharField(max_length=3, choices=funcoes, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=estados, null=False, blank=False)
    usuario = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)

    USERNAME_FIELD = "usuario"
    REQUIRED_FIELDS = ['nome', 'genero', 'funcao', 'estado', 'email']

    #Referencia para linha da tabela
    def __str__(self) -> str:
        return self.usuario