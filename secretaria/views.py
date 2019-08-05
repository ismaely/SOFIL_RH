from core_help.includes import *
from core_help.core import retorna_id

from core_help.views_pdf import(logo_pdf, pdf_cabecario, pdf_horizontal_cabeca, rodape_imagem_Vertical, rodape_numero_pagina_imagem_horizontal, gerar_pdf_simples)
# Create your views here.



@login_required
def home(request):
    context = {}
    return render (request, 'home_centro.html', context)



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


def consultar_dados_pessoal(request):
    form = Emitir_declaracao_ConsultarDados_Form(request.POST or None)
    if form.is_valid():
        print("consulta")
    lista =[]
    context = {'form':form ,'lista': lista, 'escolha': 2}
    return render (request, 'secretaria/emitir_declaracao.html', context)



def listar_dados_nominal(request):
    form = Menu_listagem_Form(request.POST or None)
    lista =[]
    if request.method == 'POST':
        if form.is_valid():
            curso = int(form.cleaned_data.get('curso'))
            grau = int(form.cleaned_data.get('grau'))
            ano = form.cleaned_data.get('ano')
            semestre = form.cleaned_data.get('semestre')
            especialidade = form.cleaned_data.get('especialidade')
            data = str(form.cleaned_data.get('data_entrada'))
            novaData = []
            
            if grau == 2 and curso > 0:
                
                # BUSCAR TUDO 
                if len(ano) > 0 and len(semestre) > 0 and len(especialidade) > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, ano_id=ano, semestre_id=semestre,data_matricula__startswith=novaData[0]).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)

                # BUCAR COM ANO, SEMESTRE, ESPECIALIDADE
                elif len(ano) > 0 and len(semestre)  > 0 and len(especialidade) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, ano_id=ano, semestre_id=semestre).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)

                # BUCAR COM ANO, SEMESTRE, DATA
                elif len(ano) > 0 and len(semestre)  > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, ano_id=ano, semestre_id=semestre, data_matricula__startswith=novaData[0]).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)

                # BUCAR COM ANO, SEMESTRE
                elif len(ano) > 0 and len(semestre) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, ano_id=ano, semestre_id=semestre).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)


                # BUCAR COM ESPECIALIDADE, ANO,
                elif len(especialidade) > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, data_matricula__startswith=novaData[0]).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)

                # BUCAR COM ESPECIALIDADE
                elif len(especialidade) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)

                # ANO,
                elif len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__startswith=novaData[0]).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)

                # APENAS CURSO
                else:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_mestrado.html', context)
            else:
                if curso > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__startswith=novaData[0]).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_posGraduacao.html', context)
                else:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso).all()
                    context = {'lista': matricula}
                    return render (request, 'secretaria/listar_estudante_posGraduacao.html', context)

    context = {'form': form, 'escolha': 1}
    return render (request, 'secretaria/menu_listagem_mestrado.html', context)



# SELECIONA O SEMESTRE ATRAVES DO ANO E RETORNA O SEMESTRE
def recebe_ano_retornaSemestre_ajax(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.id, k.nome)for k in Semestre.objects.select_related('ano').filter(ano_id=id).all()]
            dados = {
                'resposta':  lista
            }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO RETORNO SEMESTRE")



# SELECIONA O TUDO DO MESTRADO E POS-GRADUAÇÃO EM FUNCOA DO GRAU-ACADEMICO
def recebe_grau_academico_ajax(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.id, k.nome)for k in Cursos.objects.filter(grau_academico_id=int(id))]
            dados = {
                'cursos':  lista,
            }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO RETORNO CURSO POR GRAU ACADEMICO")



# SELECIONA A ESPECIALIDADE EM FUNÇÃO DO ID DO CURSO
def recebe_idCurso_retornaEspecialidadeModuloAno_ajax(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.id, k.nome)for k in Especialidade.objects.select_related('curso').filter(curso_id=id).all()]
            modulos = [(k.id, k.nome)for k in Modulo_Disciplina.objects.select_related('curso').filter(curso_id=id).all()]
            if int(id) > 2:
                ano = [(k.id, k.nome)for k in Ano.objects.all()]
                dados = {
                    'resposta':  lista,
                    'modulos':  modulos,
                    'ano': ano
                }
            else:
                dados = {
                    'resposta':  lista,
                    'modulos':  modulos
                }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO NO RETORNO CURSO ESPECIALIDADE")




#RECEBE O ID DO CURSO E RETORNA  TODOS OS MODULOS DA QUEL CURSO
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
        print("ERRO NO CURSO PARA NOTA ")



@login_required
def lancamento_nota(request):
    form = Nota_lancamento_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                curso = int(request.POST.get('curso'))
                modulo = int(request.POST.get('modulo'))
                estudante = form.cleaned_data.get('estudante')

                modu = Modulo_Disciplina.objects.select_related('curso').get(id = modulo)
                matricula = Matricula.objects.select_related('curso').get(estudante_id=estudante, curso_id= curso)

                if modu.ano_id == matricula.ano_id and modu.semestre_id == matricula.semestre_id and modu.curso_id == matricula.curso_id:
                    try:
                        notas = Nota.objects.get(estudante_id=estudante, curso_id=curso, modulo_id=modulo)
                        if notas.nota is not None:
                            sweetify.error(request, 'O estudante já tem Nota nesta cadeira! <br> Contacta o Admin!..', persistent='OK', timer='3100')
                    except Nota.DoesNotExist:
                        resp = form.save(commit=False)
                        resp.estudante_id = estudante
                        resp.curso_id = curso
                        resp.modulo_id = modulo
                        resp.matricula_id = matricula.id
                        resp.save()
                        sweetify.success(request, 'Inserido com Sucesso!..',position ='top-end', button='Ok', timer='4100')
                else:
                    if modu.curso_id == matricula.curso_id and curso > 0 and curso < 3:
                        try:
                            notas = Nota.objects.get(estudante_id=estudante, curso_id=curso, modulo_id=modulo)
                            if notas.nota is not None:
                                sweetify.error(request, 'O estudante já tem Nota nesta cadeira! <br> Contacta o Admin..!', persistent='OK', timer='3100')
                        except Nota.DoesNotExist:
                            resp = form.save(commit=False)
                            resp.estudante_id = estudante
                            resp.curso_id = curso
                            resp.modulo_id = modulo
                            resp.matricula_id = matricula.id
                            resp.save()
                            sweetify.success(request, 'Inserido com Sucesso..!', button='Ok', timer='4100')
                    else:
                        sweetify.error(request, 'Não pode ser lançada a nota porque; não fez a inscrição', position ='top-end',   persistent='OK', timer='4100')
            except Matricula.DoesNotExist:
                sweetify.error(request, 'Não pode ser lançada a nota porque, não esta inscrito na cadeira', position ='top-end',   persistent='OK')

    context = {'form':form}
    return render (request, 'secretaria/registar_lancamento_nota.html', context)



def registar_confirma_matricula(request):
    form = Matricula_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and validar_cadeira_atraso(request):
            resp = form.save(commit=False)
            print(form.cleaned_data)
            resp.estudante_id = form.cleaned_data.get('estudante')
            resp.ano_id = form.cleaned_data.get('ano')
            resp.semestre_id = form.cleaned_data.get('semestre')
            if form.cleaned_data.get('cadeira_atraso_1') is not None:
                resp.cadeira_atraso_1_id = form.cleaned_data.get('cadeira_atraso_1')
            if form.cleaned_data.get('cadeira_atraso_2') is not None:
                resp.cadeira_atraso_2_id = form.cleaned_data.get('cadeira_atraso_2')
            if form.cleaned_data.get('cadeira_atraso_3') is not None:
                resp.cadeira_atraso_3_id = form.cleaned_data.get('cadeira_atraso_3')
            if form.cleaned_data.get('cadeira_atraso_4') is not None:
                resp.cadeira_atraso_4_id = form.cleaned_data.get('cadeira_atraso_4')
            
            resp.save()
            sweetify.success(request, 'Confirmação Realizada com sucesso!....', button='Ok', timer='3100')
            return render (request, 'secretaria/sucesso_matricula.html', {'id': resp.id})
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
            if len(estu.numero_estudante) > 0:
                sweetify.error(request, 'O Estudante já tem numero de Matricula. <br> Se Deseja trocar consulta o Admin!....', persistent='OK', timer='3100')
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





#função que vai gerar a ficha de matatricula quando a matricula acabar
def imprimir_ficha_matricula(request, id_value):
    resp = Matricula.objects.select_related('estudante').get(id=id_value)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'
    buffer, p, style, estilosB = pdf_cabecario()
    texto_core = estilosB
    #p.line(100,670,500,670)
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/ficha_inscricao.png'))
    logo_pdf(p)
    p.setFontSize(14)
    p.drawImage(logo, 0, 0, width=593, height=845, mask=None)

    linha = '_________'
    for lin in range(3):
        linha += linha
    #linha de cima
    p.drawString(68,715, linha)
    # linha de baixo
    ano = []
    p.drawString(68,620, linha)
    p.drawString(250.3,690,'Recibo Nº')
    p.drawString(250.3,675, 'Confirmação de Matrícula')
    p.drawString(250.3,660,str(resp.curso.nome))
    ano = str(resp.data_matricula).split('-')
    p.drawString(250.3,645, 'Ano Lectivo: ' + str(ano[0]))
    
    nome = Paragraph(''' NOME ''',estilosB)
    numero = Paragraph(''' NÚMERO ''',estilosB)
    bi = Paragraph(''' BI Nº ''',estilosB)
    genero = Paragraph(''' GÉNERO ''',estilosB)
    
    disciplina = Paragraph(''' DADOS DA INSCRIÇÃO (Disciplinas) ''',estilosB)
    sigla = Paragraph(''' SIGLA ''',estilosB)
    nivel  = Paragraph(''' ANO ''',estilosB)
    semestre = Paragraph(''' Semestre ''',estilosB)
    cadeira = Paragraph('''  CADEIRAS EM ATRASO ''',estilosB)

    operador = Paragraph('''  OPERADOR ''',estilosB)
    valor = Paragraph('''  VALOR ''',estilosB)
    data_matricula = Paragraph('''  DATA ''',estilosB)

    data1 = []
    data2 = []
    data3 = []
    informacao = []
    data_cadeira_atraso = []

    data1.append([nome, numero])
    data2.append([bi, genero])
    data3.append([disciplina,sigla, nivel])
    data_cadeira_atraso.append([cadeira, sigla])
    informacao.append([operador, valor, data_matricula])
    #Dados pessoal
    dados1 = [str(resp.estudante.pessoa.nome).upper(), str(resp.estudante.numero_estudante).upper()]
    dados2 = [str(resp.estudante.pessoa.bi).upper(), str(resp.estudante.pessoa.genero).upper()]
    informacao.append(['','', str(resp.data_matricula)])
    #matricula
    # posgraduação
    if resp.curso_id == 1 or resp.curso_id == 2:
        for modul in Modulo_Disciplina.objects.select_related('curso').filter(curso_id=resp.curso_id).all():
            data3.append([str(modul.nome), str(modul.sigla_codigo),''])
    
    #mestrado
    if resp.curso_id == 3 or resp.curso_id == 4:
        for modul in Modulo_Disciplina.objects.select_related('curso').filter(curso_id=resp.curso_id, semestre_id=resp.semestre_id).all():
            data3.append([str(modul.nome), str(modul.sigla_codigo),str( modul.ano.nome)])

    # cadeiras em atraso
    if resp.cadeira_atraso_1_id is not None:
        data_cadeira_atraso.append([str(resp.cadeira_atraso_1.nome), str(resp.cadeira_atraso_1.sigla_codigo)])
    
    if resp.cadeira_atraso_2_id is not None:
        data_cadeira_atraso.append([str(resp.cadeira_atraso_2.nome), str(resp.cadeira_atraso_2.sigla_codigo)])
    
    if resp.cadeira_atraso_3_id is not None:
        data_cadeira_atraso.append([str(resp.cadeira_atraso_3.nome), str(resp.cadeira_atraso_3.sigla_codigo)])
    
    if resp.cadeira_atraso_4_id is not None:
        data_cadeira_atraso.append([str(resp.cadeira_atraso_4.nome), str(resp.cadeira_atraso_4.sigla_codigo)])
    
    data1.append(dados1)
    data2.append(dados2)
    width, height = A4
    # 1ª Tabela dados pessoais
    
    table1 = Table(data1, colWidths=[13.3 * cm, 4.8 * cm, 1.0 * cm, 1.0 * cm])
    table1.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
    ]))
    table1.wrapOn(p, width, height)
    table1.drawOn(p, 55, 552)

    # 2ªTabela dados pessoais
    table2 = Table(data2, colWidths=[13.3 * cm, 4.8 * cm, 1.0 * cm, 1.0 * cm])
    table2.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
    ]))
    table2.wrapOn(p, width, height)
    table2.drawOn(p, 55, 515)

    # Tabelas das diciplinas
    table3 = Table(data3, colWidths=[13.3 * cm, 2.5 * cm, 2.3 * cm, 1.0 * cm])
    table3.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
    ]))
    table3.wrapOn(p, width, height)
    table3.drawOn(p, 55, 450.7)

    # cadeiras em atraso
    if resp.cadeira_atraso_1_id is not None or resp.cadeira_atraso_2_id is not None:
        table4 = Table(data_cadeira_atraso, colWidths=[13.3 * cm, 2.5 * cm, 2.3 * cm, 1.0 * cm])
        table4.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
        table4.wrapOn(p, width, height)
        table4.drawOn(p, 55, 290.7)
    
    # informação pessoal
    table5 = Table(informacao, colWidths=[13 * cm, 3.1 * cm, 2.1 * cm, 1.0 * cm])
    table5.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
    ]))
    table5.wrapOn(p, width, height)
    table5.drawOn(p, 55, 210.7)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



# função que vai imprmir a declaração onde estamos a mexer muito
def emitir_delaracao(request):
    form = Emitir_declaracao_ConsultarDados_Form(request.POST or None)
    if form.is_valid():
        buffer = BytesIO()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'
        #p = canvas.Canvas(buffer)
        
        doc = SimpleDocTemplate(buffer,pagesize=letter, rightMargin=55,leftMargin=55,topMargin=150,bottomMargin=75)
        
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    
        Story = []
        print(doc.height)

        #logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
        ##Story.append(uan_logo)
        magName = "Pythonista"
        issueNum = 12
        subPrice = "99.00"
        limitedDate = "03/05/2010"
        freeGift = "tin foil hat"
        full_name = "Marvin Jones"
        address_parts = ["411 State St.", "Reno, NV 80158"]
 
        for page in range(10):
            # Create return address
            ptext = '<font size=12>%s</font>' % full_name
            Story.append(Paragraph(ptext, styles["Normal"]))       
            for part in address_parts:
                ptext = '<font size=12>%s</font>' % part.strip()
                Story.append(Paragraph(ptext, styles["Normal"]))
 
        Story.append(Spacer(1, 12))
        ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))
 
        ptext = """<font size=12>We would like to welcome you to our subscriber base 
        for %s Magazine! You will receive %s issues at the excellent introductory 
        price of $%s. Please respond by %s to start receiving your subscription 
        and get the following free gift: %s.</font>""" 
        ptext = ptext % (magName, issueNum, subPrice, limitedDate, freeGift)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
 
        ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size=12>Sincerely,</font>'
        Story.append(Paragraph(ptext, styles["Normal"]))
       
        Story.append(PageBreak())
        #p.showPage()
       
        doc.build(Story, onFirstPage=rodape_imagem_Vertical, onLaterPages=rodape_imagem_Vertical)
        response.write(buffer.getvalue())
        buffer.close()
        return response

    lista =[]
    context = {'form':form,'lista': lista}
    return render (request, 'secretaria/emitir_declaracao.html', context)




def gerar_lista_estudante_pdf(request):
    form = Menu_listagem_Form(request.POST or None)
    lista =[]
    if request.method == 'POST':
        if form.is_valid():
            curso = int(form.cleaned_data.get('curso'))
            grau = int(form.cleaned_data.get('grau'))
            ano = form.cleaned_data.get('ano')
            semestre = form.cleaned_data.get('semestre')
            especialidade = form.cleaned_data.get('especialidade')
            data = str(form.cleaned_data.get('data_entrada'))
            novaData = []
            
            if grau == 2 and curso > 0:
                # BUSCAR TUDO  Mestrado
                if len(ano) > 0 and len(semestre) > 0 and len(especialidade) > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, ano_id=ano, semestre_id=semestre,data_matricula__startswith=novaData[0]).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

                # BUCAR COM ANO, SEMESTRE, ESPECIALIDADE
                elif len(ano) > 0 and len(semestre)  > 0 and len(especialidade) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, ano_id=ano, semestre_id=semestre).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)


                # BUCAR COM ANO, SEMESTRE, DATA
                elif len(ano) > 0 and len(semestre)  > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, ano_id=ano, semestre_id=semestre, data_matricula__startswith=novaData[0]).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

                # BUCAR COM ANO, SEMESTRE
                elif len(ano) > 0 and len(semestre) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, ano_id=ano, semestre_id=semestre).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)


                # BUCAR COM ESPECIALIDADE, ANO,
                elif len(especialidade) > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, data_matricula__startswith=novaData[0]).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

                # BUCAR COM ESPECIALIDADE
                elif len(especialidade) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

                # ANO,
                elif len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__startswith=novaData[0]).all()
                    context = {'lista': matricula}
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

                # APENAS CURSO
                else:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)
                
            else:
                #pos-graduação
                if curso > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__startswith=novaData[0]).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)
                else:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

    context = {'form': form, 'escolha': 2}
    return render (request, 'secretaria/menu_listagem_mestrado.html', context)
