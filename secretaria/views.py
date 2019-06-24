from helper.includes import *
# Create your views here.



def login(request):
    context = {}
    return render (request, 'login.html', context)



def home(request):
    context = {}
    return render (request, 'home_centro.html', context)



def listar_dados_estudante(request):
    context = {}
    return render (request, 'secretaria/listar_dados_estudante.html', context)



def registar_confirma_matricula(request):
    context = {}
    return render (request, 'secretaria/registar_confirma_matricula.html', context)



def registar_Monografia(request):
    context = {}
    return render (request, 'secretaria/registar_Monografia.html', context)



def registar_curso(request):
    context = {}
    return render (request, 'secretaria/registar_curso.html', context)



def registar_modulo(request):
    context = {}
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
    return render (request, 'secretaria/registar_cadastro.html', context)




