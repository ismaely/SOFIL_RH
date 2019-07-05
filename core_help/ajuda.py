#
# ajuda.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 27/06/2019, 07:39:50
from core_help.includes import *




def retorna_id_recebendo_bi(value):
    try:
       bi = Pessoa.objects.get(bi=value)
       if bi.id is not None:
           return bi.id
    except Pessoa.DoesNotExist:
        return 0
