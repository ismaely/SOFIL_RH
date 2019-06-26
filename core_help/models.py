from django.db import models

"""MODELO DE AJUDA , ONDE CONSTA AS  CLASSE QUE NÃO PERTENCEM  DIREITAMENTE AO PROJETO
TODOS OS MODELOS QUE ESTAO A QUE OS DADOS SÃO INSERIDO MANUALMENTE NA BASE DE DADOS"""




class Semestre(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return  "%s" % (self.nome)



class Provincias(models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return "%s" % (self.nome)
    


class Instituicao_superior(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20, blank=True, null=True, default=" ")

    def __str__ (self):
        return "%s" % (self.nome)



class Ano_Semestre(models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=20)

    def __str__ (self):
        return "%s" % (self.nome)


class Grau_academico(models.Model):
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return "%s" % (self.nome)



class Especialidade(models.Model):
    grau_academico = models.ForeignKey(Grau_academico, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=160)

    def __str__ (self):
        return "%s" % (self.nome)