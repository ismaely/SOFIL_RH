from core_help.includes import *
from core_help.core import retorna_id
# Create your views here.


@login_required
def listar_utilizador(request):
    lista =[]
    lista = Controla_SenhaPadrao.objects.select_related('pessoa').all()
    context = {'lista': lista, 'form': Actualizar_categoria_Form(request.POST or None)}
    return render (request, 'utilizador/listar_utilizador.html', context)


@login_required
def ativar_conta(request, pk):
    if pk > 0:
        user = User.objects.get(id=pk)
        user.is_active = 1
        user.save()
        sweetify.success(request,'Conta Ativado com sucesso!....', timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))
    else:
        sweetify.info(request,'Acesso Negado!Falha....', timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))


@login_required
def desativar_conta(request, pk):
    if pk > 0:
        user = User.objects.get(id=pk)
        user.is_active = 0
        user.save()
        sweetify.success(request,'Conta Desativada com sucesso!....', timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))
    else:
        sweetify.info(request,'Acesso Negado!Falha....', timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))


@login_required
def atualizar_funcao_categoria(request, pk):
    form = Actualizar_categoria_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.get(id=pk)
            user.last_name = form.cleaned_data.get('categoria')
            user.save()
            sweetify.success(request,'Função atualizada com sucesso!....', timer='4900', button='Ok')
    return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))


def perfil_utilizador(request):
    
    context = {}
    return render (request, 'utilizador/perfil.html', context)


# função que vai receber o dados da obrigação da troca de senha quando criar a conta
def troca_senha_padrao(request):
    form = Troca_SenhaPadrao_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data.get('nome_utilizador')
            user = User.objects.get(username=nome)
            if user.id is not None:
                conta = Controla_SenhaPadrao.objects.get(user_id = user.id)
                if int(conta.estado) == 0:
                    user.set_password(form.cleaned_data.get('senha'))
                    user.save()
                    conta.estado = 1
                    conta.save()
                    if conta is not None:
                        #return HttpResponseRedirect(reverse('utilizador:sair'))
                        sweetify.success(request, 'Alteração feita com sucesso.. seja bem vindo!.', persistent='OK', timer='3100')
                return HttpResponseRedirect(reverse('utilizador:sair'))
                #sweetify.error(request, 'Acesso Negado! Verifica o seu nome...', persistent='OK', timer='3100')
            else:
                sweetify.error(request, 'Nome do Utilizador errado!.', persistent='OK', timer='3100')
    context = {'form': form}
    return render (request, 'utilizador/troca_senha.html', context)



def login_sistema(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                lista = []
                senha = form.cleaned_data.get('senha')
                nome = form.cleaned_data.get('nome_utilizador')
                resp = User.objects.get(username=nome)
                password = check_password(senha, resp.password)
                if resp.username == nome and password:
                    conta = Controla_SenhaPadrao.objects.get(user_id = resp.id)
                    if resp.is_active: 
                        if int(conta.estado) == 1:
                            user = authenticate(username=nome,password=senha)
                            login(request, user)
                            return HttpResponseRedirect(reverse('secretaria:home'))
                        else:
                            sweetify.info(request, 'A Conta esta desativada <br> Diriga-se ao Administrador!.', persistent='OK')
                            return HttpResponseRedirect(reverse('utilizador:sair'))
                    else:
                        #sweetify.info(request, 'Muda a senha da sua primeiro!.', persistent='OK', timer='3100')
                        return HttpResponseRedirect(reverse('utilizador:troca-senha-padrao'))
                else:
                    messages.warning(request, 'Dados errados!...')
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe...')

    context = {'form': form}
    return render (request, 'utilizador/login.html', context)




@login_required
def criar_conta_utilizador(request):
    #form = PessoaForm(request.POST or None)
    form = Utilizador_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            resp = retorna_id(form.cleaned_data.get('bi_2'))
            if  resp != 0:
                try:
                    user = User.objects.get(first_name=resp)
                    if user.id is not None:
                        sweetify.error(request, 'O utilizador já têm uma conta!...', persistent='OK', timer='3100')
                except User.DoesNotExist:
                    novo = User.objects.create_user(username=request.POST['nome_utilizador'], first_name=resp, last_name=request.POST['categoria'],password=SENHA_PADRAO)
                    Controla_SenhaPadrao.objects.create(user_id=novo.id, estado=0, pessoa_id=resp)
                    sweetify.success(request, 'Conta criado com sucesso..', persistent='OK', timer='3100')
                    return render (request, 'home_centro.html', {})
            else:
                sweetify.error(request, 'O utilizador não possui cadastro no sistema...', persistent='OK', timer='3100')
    context = {'form':form}
    return render (request, 'utilizador/criar_conta_utilizador.html', context)




@login_required
def registar_utilizador(request):
    form = PessoaForm(request.POST or None)
    form2 = Utilizador_Form(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid() and form2.is_valid():
                #pessoa = form.save()
                pessoa = form.save(commit=False)
                pessoa.municipio_id = form.cleaned_data.get('municipio')
                pessoa.save()
                if pessoa.id is not None:
                    user = User.objects.create_user(username=request.POST['nome_utilizador'], first_name=pessoa.id, last_name=request.POST['categoria'],email=request.POST['email'],password=SENHA_PADRAO)
                    estado = Controla_SenhaPadrao.objects.create(user_id=user.id, estado=0, pessoa_id=pessoa.id)
            sweetify.success(request, 'Conta criada com sucesso! <br> Depois o utilizador deve alterar a senha Padrão....', persistent='OK', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))
        except Exception as e:
            #print(e)
            sweetify.error(request, 'Já existe um utilizador com este nome de Utilizador!.', persistent='OK', timer='3100')
   
    context = {'form':form, 'form2':form2}
    return render (request, 'utilizador/registar_utilizador.html', context)




@login_required
def sair(request):
    try:
        #del request.session['salakiaku']
        logout(request)
        return HttpResponseRedirect(reverse('utilizador:login'))
    except Exception as e:
        raise Http404("erro a terminar a sessão %s " % (e))

