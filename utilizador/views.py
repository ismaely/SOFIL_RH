from core_help.includes import *
from core_help.core import retorna_id
# Create your views here.





# função que vai receber o dados da obrigação da troca de senha quando criar a conta
def troca_senha_padrao(request):
    form = Troca_SenhaPadrao_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            senha = form.cleaned_data.get('senha')
            nome = form.cleaned_data.get('nome_utilizador')
            ut = User.objects.get(username=nome)
            if ut.id is not None:
                conta = Controla_SenhaPadrao.objects.get(user_id = ut.id)
                ut.set_password = senha
                ut.save()
                conta.estado = 1
                conta.save()
                if conta is not None:
                   sweetify.success(request, 'Alteração feita com sucesso. <br> Já podes fazer o Login!.', persistent='OK', timer='3100')
                   return HttpResponseRedirect(reverse('utilizador:sair'))
            else:
                sweetify.error(request, 'Nome do Utilizador errado!.', persistent='OK', timer='3100')
    context = {'form': form}
    return render (request, 'utilizador/troca_senha.html', context)



def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                lista = []
                senha = form.cleaned_data.get('senha')
                nome = form.cleaned_data.get('nome_utilizador')
                user = authenticate(username=nome,password=senha)
                if user is not None:
                    conta = Controla_SenhaPadrao.objects.get(user_id = user.id)
                    if conta.estado == 1:
                        if user.is_active:
                            login(request, user)
                            return HttpResponseRedirect(reverse('secretaria:home'))
                        else:
                            sweetify.info(request, 'A Conta esta desativada <br> Diriga-se ao Administrador!.', persistent='OK')
                            return HttpResponseRedirect(reverse('utilizador:sair'))
                    else:
                        sweetify.info(request, 'Muda a senha da sua primeiro!.', persistent='OK', timer='3100')
                        return HttpResponseRedirect(reverse('utilizador:troca-senha-padrao'))
                else:
                    messages.warning(request, 'Dados errados!...')
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe...')

    context = {'form': form}
    return render (request, 'utilizador/login.html', context)



@login_required
def sair(request):
    try:
        #del request.session['salakiaku']
        logout(request)
        return HttpResponseRedirect(reverse('utilizador:login'))
    except Exception as e:
        raise Http404("erro a terminar a sessão %s " % (e))


@login_required
def registar_utilizador(request):
    form = PessoaForm(request.POST or None)
    form2 = Utilizador_Form(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid() and form2.is_valid():
                pessoa = form.save()
                if pessoa.id is not None:
                    user = User.objects.create_user(username=request.POST['nome_utilizador'], first_name=pessoa.id, last_name=request.POST['categoria'],email=request.POST['email'],password=SENHA_PADRAO)
                    estado = Controla_SenhaPadrao.objects.create(user_id=user.id, estado=0, pessoa_id=pessoa.id)
            sweetify.success(request, 'Conta criada com sucesso! <br> Depois o utilizador deve alterar a senha Padrão....', persistent='OK', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))
        except IntegrityError:
            sweetify.error(request, 'Já existe um utilizador com este nome de Utilizador!.', persistent='OK', timer='3100')
   
    context = {'form':form, 'form2':form2}
    return render (request, 'utilizador/registar_utilizador.html', context)