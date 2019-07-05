from django.db import models
from core_help.opcoes_escolha import GENERO, ESTADO_CIVIL, GRAU_ACDAEMICO_DOCENTE
from core_help.models import Provincias, Instituicao_superior, Semestre, Especialidade, Ano

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200,)
    nome_pai = models.CharField(max_length=200, blank=True, null=True, default="--")
    nome_mae = models.CharField(max_length=200, blank=True, null=True, default="--")
    genero = models.CharField(max_length=12, choices=GENERO)
    naturalidade = models.ForeignKey(Provincias, on_delete=models.CASCADE, parent_link=True)
    data_nascimento = models.DateField()
    bi = models.CharField(max_length=20, unique=True)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    residencia = models.CharField(max_length=90, blank=True, null=True, default=" ")
    telefone = models.CharField(max_length=30, blank=True, null=True, default="--")
    email = models.EmailField(max_length=60, blank=True, null=True, default="cpppgl_uan@gmail.com")
    
    def __str__(self):
        return self.id



class Estudante(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    universidade = models.ForeignKey(Instituicao_superior, on_delete=models.CASCADE, parent_link=True)
    graduado = models.CharField(max_length=90, blank=True, null=True)
    especialidade = models.CharField(max_length=90, blank=True, null=True)
    data_conclusao = models.CharField(max_length=20, blank=True, null=True)
    numero_estudante= models.CharField(max_length=30, blank=True, null=True)
    nota_final = models.CharField(max_length=2, blank=True, null=True)
    data_inscricao = models.CharField(max_length=20, blank=True, null=True)

    def __str__ (self):
        return self.id




class Docente(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    numero_docente= models.CharField(max_length=10, blank=True, null=True)
    grau_academico = models.CharField(max_length=50, choices=GRAU_ACDAEMICO_DOCENTE, blank=True, null=True)

    def __str__ (self):
        return self.id



class Funcionario(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True, blank=True, null=True)
    cargo = models.CharField(max_length=50,blank=True, null=True)
    grau_academico = models.CharField(max_length=50, choices=GRAU_ACDAEMICO_DOCENTE, blank=True, null=True)
    
    def __str__ (self):
        return self.id




class Profissao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    instituicao = models.CharField(max_length=190, blank=True, null=True, default="--")
    funcao = models.CharField(max_length=190, blank=True, null=True, default="--")
    area_profissional = models.CharField(max_length=120, blank=True, null=True, default="--")
    ano_experiencia = models.CharField(max_length=9, blank=True, null=True, default="--")
    localizacao = models.CharField(max_length=50, blank=True, null=True)

    def __str__ (self):
        return self.id



class Modulo_Disciplina(models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    nome = models.CharField(max_length=190, blank=True, null=True, default="--")
    sigla_codigo = models.CharField(max_length=190, blank=True, null=True, default="--")
    Horas = models.CharField(max_length=12, blank=True, null=True, default="--")
    credito = models.CharField(max_length=9, blank=True, null=True, default="--")
    estado = models.CharField(max_length=19, blank=True, null=True, default="Ativado")

    def __str__ (self):
        return self.id



class Monografia(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    docente = models.CharField(max_length=90, blank=True, null=True, default="--")
    tema = models.CharField(max_length=190, blank=True, null=True, default="--")
    data_entrada = models.DateField()
    estado = models.CharField(max_length=30, blank=True, null=True, default="Recebido")
    descricao = models.CharField(max_length=90, blank=True, null=True, default="--")

    def __str__ (self):
        return self.id