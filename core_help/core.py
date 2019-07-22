# core.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 12/07/2019, 14:05:52
from secretaria.models import Pessoa, Estudante, Profissao, Modulo_Disciplina


# recebe valor e retorna id 
def retorna_id(value):
    try:
        lu = dict()
        bi = Pessoa.objects.get(bi=value)
        if bi.id is not None:
            try:
                lu = Estudante.objects.get(pessoa_id=bi.id)
                if lu.id is not None:
                    return lu.id
            except Estudante.DoesNotExist:
                #sweetify.error(request,'O Numero do Aluno não é valido!....', timer='4900', button='Ok')
                return 0
    except Pessoa.DoesNotExist:
        try:
            alu = Estudante.objects.get(numero_estudante=value)
            return alu.id
        except Estudante.DoesNotExist:
            #sweetify.error(request,'O Numero de Aluno não é valido!....', timer='4900', button='Ok')
            return 0


