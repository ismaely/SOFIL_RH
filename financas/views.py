from core_help.includes import *
from core_help.core import retorna_id
from core_help.views_pdf import(logo_pdf, pdf_cabecario, rodape_imagem_Vertical, rodape_factura)

# Create your views here.


@login_required
def listar_pagamento(request):
    form = Listar_PagamentoForm(request.POST or None)
    lista =[]
    if request.method == 'POST':
         if form.is_valid():
            data = str(form.cleaned_data.get('data_entrada'))
            # data[:-3] -> 2019-02
            lista = Pagamento.objects.select_related('grau').filter(data_pagamento__startswith=data[:-3]).all()
            context = {'lista': lista}
            return render(request, 'financa/listar_pagamentos.html', context)
    
    context = {'form':form, 'escolha': 1}
    return render(request, 'financa/menu_listar_pagamento.html', context)


@login_required
def listar_dividas(request):
    form = Listar_PagamentoForm(request.POST or None)
    lista =[]
    if request.method == 'POST':
        if form.is_valid():
            data = str(form.cleaned_data.get('data_entrada'))
            novaData = [data.split('-')]
            lista = Pagamento.objects.select_related('grau').filter(data_matricula__startswith=novaData[0]).all()
            context = {'lista': lista}
            return render(request, 'financa/listar_pagamentos.html', context)
    #lista = Pagamento.objects.order_by('-id')
    context = {'form':form}
    return render (request, 'financa/menu_listar_pagamento.html', context)


@login_required
# registar pagamento qualquer tipo
def registar_Pagamento(request):
    form = PagamentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.estudante_id = form.cleaned_data.get('estudante')
            pagamento.save()
            #sweetify.success(request, 'Pagamento Registado com sucesso!....', position ='top-end',  button='Ok', timer='4000')
            context = {'id': pagamento.id}
            return render (request, 'financa/sucesso_pagamento.html', context )

    context = {'form':form}
    return render (request, 'financa/registar_pagamento.html', context)


@login_required
# gerar factura de pagamento
def imprmir_fatura_pagamento(request, id):
    matricula = []
    resp = Pagamento.objects.select_related('estudante').get(id=id)
    matricula = Matricula.objects.filter(estudante_id=resp.estudante_id)
    #print(matricula.query)
    
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Factura.pdf"'
    #p = canvas.Canvas(buffer)
    doc = SimpleDocTemplate(buffer,pagesize=letter, rightMargin=55,leftMargin=55,topMargin=150,bottomMargin=75)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    Dados = []
    TABELA = []
    TABELA_TOTAL= []
    DADOS =[]
    DADOS_TOTAL = []
    LEGENDA =""
    LEGENDA=('DESCRIÇÃO',  'UNIDADE','VALOR')

    TOTAL_LEGENDA = ('TOTAL', str(resp.valor))

    if resp.grau.nome == 'Pós-Graduação':
        if resp.tipo_id is not None:
            valor = float(resp.valor ) - float(resp.tipo.valor)
            #print('{2:16.8f}' format(valor))
            DADOS.append([str(resp.tipo.tipo),' ########## ',str(resp.tipo.valor)])
            DADOS.append([str(resp.parecela_posgraduacao.nome),' ########## ', str('%f'%(valor))])
           
        else:
            DADOS.append([str(resp.parecela_posgraduacao.nome),' ########## ', str(resp.valor)])
    else:
        if resp.tipo_id is not None:
            valor = float(resp.valor ) - float(resp.tipo.valor)
            #print('{2:16.8f}' format(valor))
            DADOS.append([str(resp.tipo.tipo),' ########## ',str(resp.tipo.valor)])
            DADOS.append([str(resp.parecela_mestrado.nome),' ########## ', str('%f'%(valor))])
           
        else:
            DADOS.append(['########',' ##########', str(resp.valor)])


    exmo = "<font size=12>Comprovativo de Pagamento</font>"
    nome = "<font size=12>%s</font>" % (str(resp.estudante.pessoa.nome))
    grau = '<font size=12>Grau: %s</font>' % (str(resp.grau.nome))
    curso = '<font size=12>Curso: %s</font>' % ('')

    if resp.estudante.numero_estudante is not None:
        
        aluno = '<font size=12>Aluno Nº: %s</font>' % (str(resp.estudante.numero_estudante))
    else:
        aluno = '<font size=12>BI Nº: %s</font>' % (str(resp.estudante.pessoa.bi))
    #p.drawString(13.9*cm, 17.1* cm,'vida feita')

    Dados.append(Spacer(1, 85))
    Dados.append(Paragraph(exmo,styles["Normal"]))
    Dados.append(Spacer(1, 13))
    Dados.append(Paragraph(nome,styles["Normal"]))
    Dados.append(Spacer(1, 5))
    Dados.append(Paragraph(aluno,styles["Normal"]))
    Dados.append(Spacer(1, 5))
    Dados.append(Paragraph(grau, styles["Normal"]))
    Dados.append(Spacer(1, 5))
    Dados.append(Paragraph(curso, styles["Normal"]))
    Dados.append(Spacer(1, 20))
    
    TABELA = Table([LEGENDA] + DADOS,colWidths=[8.5 * cm, 3.2 * cm, 4.2 * cm])
    TABELA.setStyle(TableStyle([
        ('ALIGN',(0,0),(0,0),'CENTER'),
        ('GRID', (0, 0), (6, -1), 1,  colors.silver),
        ('LINEBELOW', (0, 0), (-1, 0), 1.2, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]
     ))
    TABELA_TOTAL = Table([TOTAL_LEGENDA] + DADOS_TOTAL,colWidths=[8.2 * cm,7.7 * cm,  7.2 * cm])
    TABELA_TOTAL.setStyle(TableStyle([
        ('ALIGN',(0,0),(0,0),'CENTER'),
        ('GRID', (0, 0), (4, -1), 1,  colors.silver),
        ('LINEBELOW', (0, 0), (-1, 0), 1.2, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('SPAN',(0,2),(1,2)),
        ]
     ))

    Dados.append(TABELA)
    Dados.append(Spacer(1, 1))
    Dados.append(TABELA_TOTAL)
    Dados.append(PageBreak())
    #p.showPage()
    
    doc.build(Dados, onFirstPage=rodape_factura)
    response.write(buffer.getvalue())
    buffer.close()
    return response
        