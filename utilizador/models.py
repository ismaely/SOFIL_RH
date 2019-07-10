from django.db import models
from django.contrib.auth.models import User
from secretaria.models import Pessoa
# Create your models here.

"""
Moelo que vai ter o valor do usuario que troco a senha que foi criada a sua coonta
codição do estado
1-activo troco a senha padrao
0- nao troco a senha
"""

class Controla_SenhaPadrao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, parent_link=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    estado = models.CharField(max_length=1)

    def __str__ (self):
        return self.id