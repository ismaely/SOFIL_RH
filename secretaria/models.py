from django.db import models
from core_help.opcoes_escolha import GENERO, ESTADO_CIVIL, GRAU_ACDAEMICO_DOCENTE, OPCAO_NOTA
from core_help.models import Provincias, Instituicao_superior, Semestre, Especialidade, Ano, Cursos, Municipio, Descricao_Nota
from SOFIL_RH.settings import DATE_FORMAT, DATE_INPUT_FORMATS

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
    residencia = models.CharField(max_length=90, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True, default="--")
    email = models.EmailField(max_length=60, blank=True, null=True, default="cpppgl_uan@gmail.com")
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, parent_link=True)
    
    def __str__(self):
        return self.id



class Estudante(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    universidade = models.ForeignKey(Instituicao_superior, on_delete=models.CASCADE, parent_link=True)
    graduado = models.CharField(max_length=90, blank=True, null=True)
    especialidade = models.CharField(max_length=90, blank=True, null=True)
    data_conclusao = models.CharField(max_length=20, blank=True, null=True)
    numero_estudante= models.CharField(max_length=30, blank=True, null=True, default="NULL")
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



class Modulo_Disciplina(models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=190)
    sigla_codigo = models.CharField(max_length=190, blank=True, null=True, default="--")
    Horas = models.CharField(max_length=20, blank=True, null=True, default="")
    credito = models.CharField(max_length=9, blank=True, null=True, default="--")
    estado = models.CharField(max_length=19, blank=True, null=True, default="Ativado")
    #tipo = models.CharField(max_length=19, blank=True, null=True, default="")

    def __str__ (self):
        return  "%s -> %s" % (self.nome, self.tipo)



class Monografia(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, parent_link=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)
    docente = models.CharField(max_length=90, blank=True, null=True, default="--")
    tema = models.CharField(max_length=190, default="--")
    data_entrada = models.DateField()
    estado = models.CharField(max_length=30, blank=True, null=True, default="Recebido")
    arquivo = models.FileField(upload_to='monografia', blank=True, null=True) 

    def __str__ (self):
        return self.id



class Gerar_Numero_Matricula(models.Model):
    numero = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__ (self):
        return self.id



class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, parent_link=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    cadeira_atraso_1 = models.ForeignKey(Modulo_Disciplina, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    cadeira_atraso_2 = models.ForeignKey(Modulo_Disciplina, on_delete=models.CASCADE, related_name ='cadeira2_chave_modulo', blank=True, null=True, parent_link=True)
    cadeira_atraso_3 = models.ForeignKey(Modulo_Disciplina, on_delete=models.CASCADE, related_name ='chave_cadeira3_modulo', blank=True, null=True, parent_link=True)
    cadeira_atraso_4 = models.ForeignKey(Modulo_Disciplina, on_delete=models.CASCADE, related_name ='cadeira4_modulo_chave', blank=True, null=True, parent_link=True)
    data_matricula = models.DateField()

    def __str__ (self):
        return self.id



class Nota(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, parent_link=True)
    descricao = models.ForeignKey(Descricao_Nota, on_delete=models.CASCADE, parent_link=True)
    modulo = models.ForeignKey(Modulo_Disciplina, on_delete=models.CASCADE, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    nota = models.CharField(max_length=2)
    data_entrada = models.DateField()
    data_registo_automatico = models.DateField(auto_now=True)

    def __str__ (self):
        return self.id
    
    
class Nota_final_Monografia(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, parent_link=True)
    nota = models.CharField(max_length=2)
    descricao = models.ForeignKey(Descricao_Nota, on_delete=models.CASCADE, parent_link=True)
    data_defesa = models.DateField()
    data_registo_automatico = models.DateField(auto_now=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)

    def __str__ (self):
        return self.id