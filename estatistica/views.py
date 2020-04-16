#from django.shortcuts import render
from core_help.includes import *
from estatistica.forms import Estatistica_Mestrado_Form

# Create your views here.

#estatistica_mestrado
@login_required
def menu_geral_mestrado(request):
    form = Estatistica_Mestrado_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            titulo = form.cleaned_data.get('titulo')
            curso = form.cleaned_data.get('curso')
            especialidade = form.cleaned_data.get('especialidade')
            semestre = form.cleaned_data.get('semestre')
            ano = form.cleaned_data.get('ano')
            opcao = int(form.cleaned_data.get('opcao'))
            data_incial = form.cleaned_data.get('data_incial')
            data_final = form.cleaned_data.get('data_final')
            total_curso = 0
            total_especialidade = 0
            total_masculino = 0
            total_femenino= 0
            total_ano = 0
            total_opcao = 0
            DUPLICADO = []
            
            if curso and especialidade and ano and data_incial and data_final and opcao > 1:
                resp = Nota_final_Monografia.objects.select_related('estudante').filter(curso_id=curso, especialidade_id=especialidade).all()
                dados = resp.filter(data_defesa__range=(data_incial, data_final)).all()
                total_especialidade = len(resp)
                total_curso= len(resp)
                total_opcao  = len(dados)
                for item in dados:
                    if item.estudante.pessoa.genero == 'M':
                        total_masculino = +1
                    else:
                        total_femenino =+1
               
            
            context = {'form': form, 'total_curso': total_curso, 'total_especialidade': total_especialidade,
                       'total_opcao': total_opcao, 'total_masculino': total_masculino, 'total_femenino':total_femenino, 'titulo': titulo }
            return render (request, 'estatistica/estatistica_mestrado.html', context)
    
    context = {'form': form}
    return render (request, 'estatistica/menu_geral_mestrado.html', context)