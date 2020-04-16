# core.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 12/07/2019, 14:05:52
from secretaria.models import Pessoa, Estudante, Profissao, Modulo_Disciplina


# recebe valor e retorna id 
def retorna_id(value):
    try:
        resp = Estudante.objects.get(pessoa__bi=value)
        if resp.id:
            return resp.id
            #sweetify.error(request,'O Numero do Aluno não é valido!....', timer='4900', button='Ok')
    except Estudante.DoesNotExist:
        try:
            resp = Estudante.objects.get(numero_estudante=value)
            if resp.id:
                return resp.id
        except Estudante.DoesNotExist:
            #sweetify.error(request,'O Numero de Aluno não é valido!....', timer='4900', button='Ok')
            return 0



def retorna_id_estudante(value):
    try:
        bi = Pessoa.objects.get(bi=value)
        if bi.id is not None:
            alu = Estudante.objects.get(pessoa_id=bi.id)
            if alu.id is not None:
                return alu.id
    except Pessoa.DoesNotExist:
        try:
            alu = Estudante.objects.get(numero_estudante=value)
            if alu.id:
                return alu.id
        except Estudante.DoesNotExist:
            #sweetify.error(request,'O Numero de Aluno não é valido!....', timer='4900', button='Ok')
            return 0

