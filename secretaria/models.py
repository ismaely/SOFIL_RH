from django.db import models
from helper.opcoes_escolha import GENERO, ESTADO_CIVIL, CATEGORIA_ESTUDANTE, SEMESTRE, ANO_NIVEL

# Create your models here.




class Provincia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return "%s" % (self.nome)



class Instituicao_superior(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20, blank=True, null=True, default=" ")

    def __str__ (self):
        return "%s" % (self.nome)

    

class Pessoa(models.Model):
    nome = models.CharField(max_length=200,)
    nome_pai = models.CharField(max_length=200, blank=True, null=True, default="--")
    nome_mae = models.CharField(max_length=200, blank=True, null=True, default="--")
    genero = models.CharField(max_length=12, choices=GENERO)
    naturalidade = models.ForeignKey(Provincia, on_delete=models.CASCADE, parent_link=True)
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



class Profissao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    instituicao = models.CharField(max_length=190, blank=True, null=True, default="--")
    funcao = models.CharField(max_length=190, blank=True, null=True, default="--")
    area_profissional = models.CharField(max_length=120, blank=True, null=True, default="--")
    ano_experiencia = models.CharField(max_length=9, blank=True, null=True, default="--")
    localizacao = models.CharField(max_length=50, blank=True, null=True)

    def __str__ (self):
        return self.id



class Modulo(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20, blank=True, null=True, default="--")
    carga_horaria = models.CharField(max_length=20, blank=True, null=True)
    ano = models.CharField(max_length=20, choices=ANO_NIVEL)
    semestre = models.CharField(max_length=20, choices=SEMESTRE)

    def __str__ (self):
        return self.id