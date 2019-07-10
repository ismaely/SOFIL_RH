from core_help.includes import *
from core_help.ajuda import retorna_id_recebendo_bi
# Create your views here.




def home(request):
    context = {}
    return render (request, 'home_centro.html', context)



def listar_dados_estudante(request):
    lista =[]
    lista = Estudante.objects.select_related('pessoa').all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_dados_estudante.html', context)



def listar_modulos(request):
    lista =[]
    lista = Modulo_Disciplina.objects.select_related('semestre').all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_modulos.html', context)



def registar_confirma_matricula(request):
    context = {}
    return render (request, 'secretaria/registar_confirma_matricula.html', context)

 

def registar_Monografia(request):
    form = MonografiaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.estudante_id = retorna_id_recebendo_bi(request.POST.get('estudante'))
            pessoa.save()
            sweetify.success(request, 'Modulo Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form':form,}
    return render (request, 'secretaria/registar_Monografia.html', context)



def registar_modulo(request):
    form = Modulo_DisciplinaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pessoa = form.save()
            sweetify.success(request, 'Modulo Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form':form,}
    return render (request, 'secretaria/registar_modulo.html', context)




def registar_cadastro(request):
    form = PessoaForm(request.POST or None) 
    form2 = EstudanteForm(request.POST or None)
    form3 = ProfissaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            pessoa = form.save()
            estudante = form2.save(commit=False)
            estudante.pessoa_id = pessoa.id
            estudante.save()
            profissao = form3.save(commit=False)
            profissao.estudante_id = estudante.id
            profissao.save()
            sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))
   
    context = {'form':form, 'form2': form2, 'form3': form3}
    return render (request, 'secretaria/registar_cadastro_estudante.html', context)




