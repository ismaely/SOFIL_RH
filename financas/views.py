from core_help.includes import *
from core_help.core import retorna_id
from core_help.views_pdf import(logo_pdf, pdf_cabecario, rodape_imagem_Vertical)

# Create your views here.



def listar_pagamento(request):
    lista =[]
    #lista = Pagamento.objects.order_by('-id')
    context = {'lista': lista}
    return render(request, 'financa/listar_pagamentos.html', context)


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



# gerar factura de pagamento
def imprmir_fatura_pagamento(request, id):
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'
    #p = canvas.Canvas(buffer)
    
    doc = SimpleDocTemplate(buffer,pagesize=letter, rightMargin=55,leftMargin=55,topMargin=150,bottomMargin=75)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    Story = []

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
        