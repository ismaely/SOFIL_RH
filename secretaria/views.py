from core_help.includes import *
from core_help.core import retorna_id
# Create your views here.




def home(request):
    context = {}
    return render (request, 'home_centro.html', context)



def listar_dados_estudante(request):
    lista =[]
    lista = Estudante.objects.select_related('pessoa').all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_dados_estudante.html', context)



def listar_monografia_mestrado(request):
    lista = []
    lista = Monografia.objects.select_related('curso').filter(curso_id__in = [3, 4]).all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_monografia_mestrado.html', context)



def listar_monografia_posGraduacao(request):
    lista =[]
    lista = Monografia.objects.select_related('curso').filter(curso_id__in = [1, 2]).all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_monografia_posGraduacao.html', context)


def listar_modulos_mestrado(request):
    lista =[]
    lista = Modulo_Disciplina.objects.select_related('semestre').filter(tipo='mestrado').all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_modulos_mestrado.html', context)



def listar_modulos_posGraduacao(request):
    lista =[]
    lista = Modulo_Disciplina.objects.select_related('semestre').filter(tipo='pos-graduacao').all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_modulos_posgraduacao.html', context)



def recebe_id_curso_ajax(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.id, k.nome)for k in Modulo_Disciplina.objects.select_related('curso').filter(curso_id=id).all()]
            dados = {
                    'resposta':  lista
            }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO NO CURSO PARA NOTA ")



#  REGISTAR A NOTA DO ESTUDANTE VIA AJAX
def registar_nota_ajax(request):
    dados = dict()
    if request.method == 'POST':
        valor = []
        valor = request.body.decode('utf-8')
        valor = json.loads(valor)
        estudante = retorna_id(valor['estudante'])
        if int (estudante) > 0:
            if int(valor['nota']) >= 0 and int(valor['nota']) <= 20:
                if int(valor['curso']) > 0 and int(valor['curso']) < 3 and len(valor['especialidade']) > 0:
                    sweetify.error(request, 'Pós-Graduação não possui especialidade,remove a especialidade!..', button='Ok', timer='4100')
                    dados = {
                    'resposta':  'error'
                    }
                else:
                    try:
                        resp = Nota.objects.select_related('curso').get(estudante_id=estudante, modulo_id =valor['modulo'])
                        if resp.estudante_id is not None and int(resp.curso_id) == int(valor['curso']) and int(resp.modulo_id)==int(valor['modulo']):
                            sweetify.error(request, 'O Estudante já têm Nota nesse modulo!. <br> Consulta o Admin para alterar', persistent='OK', timer='4000')
                        elif int(resp.curso_id) != int(valor['curso']):
                            Nota.objects.create(estudante_id=estudante,curso_id=valor['curso'], especialidade_id=valor['especialidade'], modulo_id=valor['modulo'], nota=valor['nota'], data_entrada=valor['data'])
                            sweetify.success(request, 'Inserido com Sucesso no !..', button='Ok', timer='4100')
                    except Nota.DoesNotExist:
                        Nota.objects.create(estudante_id=estudante,curso_id=valor['curso'], especialidade_id=valor['especialidade'], modulo_id=valor['modulo'], nota=valor['nota'], data_entrada=valor['data'])
                        sweetify.success(request, 'Inserido com Sucesso..', button='Ok', timer='4100')
                        dados = {
                        'resposta':  'error',
                        'msg': 'Inserido com Sucesso '
                        }
                   
            else:
                sweetify.error(request, 'A Nota não é valida..', button='Ok', timer='4000')
                dados = {
                'resposta':  'error'
                }
        else:
            sweetify.error(request, 'O Numero do Estudante Não é Valido....', button='Ok', timer='4000')
            dados = {
                'resposta':  'error'
            }
    return JsonResponse(dados)



def lancamento_nota(request):
    form = Nota_lancamento_Form(request.POST or None)

    context = {'form':form,}
    return render (request, 'secretaria/registar_lancamento_nota.html', context)



def registar_confirma_matricula(request):
    form = Matricula_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            id = retorna_id(request.POST['estudante'])
            resp = form.save(commit=False)
            resp.estudante_id = id
            resp.save()
            sweetify.success(request, 'Confirmação Realizada com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))
    context = {'form':form}
    return render (request, 'secretaria/registar_confirma_matricula.html', context)






def gerar_numeroEstudante(request):
    form = Gerar_numeroEstudante_Form(request.POST or None)
    if form.is_valid():
        try:
            prog = re.compile('.')
            bs = re.findall(prog, request.POST['bi'])
            parte_bi = bs[9:]
            retu = retorna_id(request.POST['bi'])
            estu = Estudante.objects.get(pessoa_id=retu)
            print(len(estu.numero_estudante))
            if len(estu.numero_estudante) > 0:
                sweetify.info(request, 'O Estudante já tem numero de Matricula. <br> Se Deseja trocar consulta o Admin!....', persistent='OK', timer='3100')
            else:
                resp = Gerar_Numero_Matricula.objects.first()
                xl = int(resp.numero) + 1
                resp.numero = xl
                novo_numero = str(xl)
                resp.save()
                for k in parte_bi:
                    novo_numero += k
                estu.numero_estudante = novo_numero
                estu.save()
                sweetify.success(request, 'Número atribuido com sucesso....', persistent='OK', timer='3100')
                context={'dados': estu, 'numero': novo_numero}
                return render (request, 'secretaria/sucesso_numero_estudante.html', context)
        except Exception as e:
            print(e)
   
    context = {'form':form}
    return render (request, 'secretaria/gerar_numero.html', context)



def registar_Monografia(request):
    form = MonografiaForm(request.POST or None)
    if request.method == 'POST':
        form = MonografiaForm(request.POST, request.FILES)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.estudante_id = retorna_id(request.POST.get('estudante'))
            pessoa.save()
            sweetify.success(request, 'Monografia cadastrado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form':form,}
    return render (request, 'secretaria/registar_Monografia.html', context)



def registar_modulo_mestrado(request):
    form = Modulo_MestradoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.tipo ='Mestrado'
            pessoa.curso_id = request.POST['curso']
            pessoa.save()
            sweetify.success(request, 'Modulo Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form':form,}
    return render (request, 'secretaria/registar_modulo_mestrado.html', context)



def registar_modulo_posGraduacao(request):
    form = Modulo_PosGraduacaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.curso_id = request.POST['curso']
            pessoa.tipo='Pós-Graduação'
            pessoa.save()
            sweetify.success(request, 'Modulo Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form':form,}
    return render (request, 'secretaria/registar_modulo_posgraducao.html', context)




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


#função que vai criar o topo do cabeçario do ficheiro pdf
def pdf_cabecario():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont('Times-Roman', 12)

    logo = os.path.join(settings.MEDIA_ROOT, str('logo/direito.jpg'))
    p.drawImage(logo, 251.5, 747, width=80, height=70, mask=None)

    p.drawString(220,737,'Universidade Agostinho Neto')
    p.drawString(239.6,723,'Faculdade de Direito')
    p.drawString(238.3,709,'Centro de Excelência')
    p.drawString(135,695,'Centro de Pesquisa em Políticas Públicas E Governação Local')
    #p.drawString(142,681,'DIRECÇÃO PROVÍNCIAL DE RECURSOS HUMANOS')
    p.line(100,670,500,670)

    style = getSampleStyleSheet()
    estilosB = style["Normal"]
    estilosB.alignment = TA_LEFT
    estilosB.fontSize = 11
    estilosB.fontName = 'Times-Roman'

    return (buffer, p, style, estilosB)



def emitir_delaracao(request):
    form = Emitir_declaracao_Form(request.POST or None)
    if form.is_valid():
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'

        buffer, p, style, estilosB = pdf_cabecario()

        p.showPage()
        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    lista =[]
    context = {'form':form,'lista': lista}
    return render (request, 'secretaria/emitir_declaracao.html', context)

