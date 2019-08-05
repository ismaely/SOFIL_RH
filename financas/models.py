from django.db import models
from secretaria.models import Pessoa, Estudante, Profissao
from core_help.models import Grau_academico
from core_help.opcoes_escolha import  GRAU_PAGAMENTO



# Create your models here.
class Categoria(models.Model):
    tipo = models.CharField(max_length=30)
    valor = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.tipo)


class Parcela_Mestrado(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.nome)


class Parcela_Pos_Graduacao(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.nome)



class Pagamento(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    grau = models.ForeignKey(Grau_academico, on_delete=models.CASCADE, parent_link=True)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE, parent_link=True, blank=True, null=True, default="")
    parecela_mestrado = models.ForeignKey(Parcela_Mestrado, on_delete=models.CASCADE, parent_link=True, blank=True, null=True, default="")
    parecela_posgraduacao = models.ForeignKey(Parcela_Pos_Graduacao, on_delete=models.CASCADE, parent_link=True, blank=True, null=True, default="")
    valor = models.CharField(max_length=13)
    data_pagamento = models.DateField()
    data_sistema = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.id


#modalidade de pagamento


