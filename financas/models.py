from django.db import models
from secretaria.models import Pessoa, Estudante, Profissao
from core_help.models import Pagamento_semestre
from core_help.opcoes_escolha import  GRAU_PAGAMENTO

# Create your models here.

class Pagamento(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, parent_link=True)
    semestre = models.ForeignKey(Pagamento_semestre, on_delete=models.CASCADE, parent_link=True)
    valor = models.CharField(max_length=10, default="--")
    data_pagamento = models.DateField()
    data_sistema = models.DateField(auto_now_add=True, blank=False, null=True)
    grau_pagamento = models.CharField(max_length=20, choices=GRAU_PAGAMENTO)

    def __str__ (self):
        return self.id