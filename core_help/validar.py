#
# validar.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 27/07/2019, 00:24:31
import random, json, re, os, sweetify

def validar_cadeira_atraso(request):
    cadeira1 = request.POST.get('cadeira_atraso_1')
    cadeira2 = request.POST.get('cadeira_atraso_2')
    cadeira3 = request.POST.get('cadeira_atraso_3')
    cadeira4 = request.POST.get('cadeira_atraso_4')
    try:
        if (cadeira1 == cadeira2 and len(cadeira1) > 0) or (cadeira1 == cadeira3 and len(cadeira1) > 0) or (cadeira1 == cadeira4 and len(cadeira1) > 0):
            sweetify.error(request, 'As Cadeiras em atraso não podem ser igual....', persistent='OK', timer='3100')
            return False
        elif(cadeira2 == cadeira3 and len(cadeira2) > 0) or (cadeira2 == cadeira4 and len(cadeira2) > 0):
            sweetify.error(request, 'As Cadeiras em atraso não podem ser igual....', persistent='OK', timer='3100')
            return False
        elif (cadeira3 == cadeira4 and len(cadeira3) > 0):
            sweetify.error(request, 'As Cadeiras em atraso não podem ser igual....', persistent='OK', timer='3100')
            return False
        else:
            return True
    except TypeError:
        return True