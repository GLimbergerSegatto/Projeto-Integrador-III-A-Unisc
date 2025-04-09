from django.db import models

class Funcionario(models.Model):

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
    
    estado = [
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
    genero = models.CharField(max_length=1, choices=generos, null=True, blank=True)
    funcao = models.CharField(max_length=3, choices=funcoes, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=estado, null=True, blank=True)
    usuario = models.CharField(max_length=50, unique=True, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)

    #Referencia para linha da tabela
    def __str__(self) -> str:
        return self.usuario