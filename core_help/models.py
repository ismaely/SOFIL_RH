from django.db import models

"""MODELO DE AJUDA , ONDE CONSTA AS  CLASSE QUE NÃO PERTENCEM  DIREITAMENTE AO PROJETO
TODOS OS MODELOS QUE ESTAO A QUE OS DADOS SÃO INSERIDO MANUALMENTE NA BASE DE DADOS"""



class Descricao_Nota(models.Model):
    valor = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return "%s" % (self.nome)


class Ano(models.Model):
    nome = models.CharField(max_length=20)

    def __str__ (self):
        return "%s" % (self.nome)


class Semestre(models.Model):
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=100,  blank=True, null=True)

    def __str__(self):
        return  "%s" % (self.nome)



class Provincias(models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return "%s" % (self.nome)



class Municipio(models.Model):
    provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return "%d" % (self.id)



class Instituicao_superior(models.Model):
    nome = models.CharField(max_length=190)
    sigla = models.CharField(max_length=20, blank=True, null=True, default=" ")

    def __str__ (self):
        return "%s" % (self.nome)



class Grau_academico(models.Model):
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return "%s" % (self.nome)



class Cursos(models.Model):
    grau_academico = models.ForeignKey(Grau_academico, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=190)

    def __str__ (self):
        return "%s -> %s" % (self.nome, self.grau_academico.nome)



class Especialidade(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=160)

    def __str__ (self):
        return "%s" % (self.nome)


#MODEL QUE VAI AUXILIAR AS OPÇÃO DA ESTATISTICA NO CAMPO OPÇÃO
class Estatistica_Opcao(models.Model):
    nome = models.CharField(max_length=100,  default="------")

    def __str__(self):
        return  "%s" % (self.nome)