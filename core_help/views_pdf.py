# views_pdf.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 29/07/2019, 17:23:33
from core_help.includes import *




def logo_pdf(p):
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
    p.drawImage(logo, 0, 0, width=593, height=845, mask=None)
    


#função que vai criar o topo do cabeçario do ficheiro pdf EM VERTICAL 
def pdf_cabecario():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont('Times-Roman', 12)

    #p.line(100,670,500,670)
    style = getSampleStyleSheet()
    estilosB = style["Normal"]
    estilosB.alignment = TA_LEFT
    estilosB.fontSize = 12
    estilosB.fontName = 'Times-Roman'
    return (buffer, p, style, estilosB)


# CADEÇARIO PARA FICHEIROS DO LOGO NA POSCIÇÃO HORIZONTAL 
def pdf_horizontal_cabeca(response):
    buffer = BytesIO()
    #p = canvas.Canvas(response, pagesize=(landscape(letter)))
    p = canvas.Canvas(response)
    p.setPageSize((10.9*inch, 7.7*inch))
    p.setFont('Times-Roman', 12)
    
    style = getSampleStyleSheet()
    estilosB = style["Normal"]
    estilosB.alignment = TA_LEFT
    estilosB.fontSize = 12
    estilosB.fontName = 'Times-Roman'
    return (buffer, p, style, estilosB)
 


def rodape_imagem_Vertical(canvas, doc):
    
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
    canvas.drawImage(logo, 0, 15, width=580, height=764, mask=None)
    page_num = canvas.getPageNumber()
    #text = "Pagina #%s" % page_num
    #canvas.drawRightString(200*mm, 20*mm, text)



def rodape_numero_pagina_imagem_horizontal(canvas, doc):
    canvas.setPageSize((10.9*inch, 7.7*inch))
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
    canvas.drawImage(logo, 0, 15, width=580, height=534, mask=None)
    page_num = canvas.getPageNumber()
    text = "Pagina #%s" % page_num
    canvas.drawRightString(256*mm, 20*mm, text)




def gerar_pdf_simples(value):
    
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Lista_Nominal.pdf"'
    #p = canvas.Canvas(buffer)
    doc = SimpleDocTemplate(buffer,pagesize=letter, rightMargin=-80,leftMargin=20,topMargin=340,bottomMargin=75)
    #print(doc.height)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    LISTA = []
    TABELA = []
    DADOS =[]
    LEGENDA =""
    
    #ptext = '<font size=12>%s</font>' % 'LISTA NOMINAL'
    estilo = ParagraphStyle('TITULO', alignment = TA_CENTER ,fontSize = 12, fontName="Times-Roman")
    ptext =Paragraph('LISTA NOMINAL',estilo)
    LISTA.append(ptext)
    LISTA.append(Spacer(1, 12))

    if value['grau'] == 2:
        if len(value['esp']) > 0:
            for cont, k in enumerate(value['lista'], 1):
                DADOS.append([cont,  str(k.estudante.pessoa.nome), str(k.estudante.pessoa.genero).upper(),  str(k.curso.nome), str(k.especialidade.nome), str(k.ano.nome).upper()])
            
            LEGENDA=('#', 'NOME', 'GENERO', 'CURSO', 'ESPECIALIDADE', 'ANO')
            TABELA = Table([LEGENDA] + DADOS)
            TABELA.setStyle(TableStyle([
                    ('ALIGN',(0,0),(0,0),'CENTER'),
                    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
                    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
                ]
            ))
        else:
            for cont, k in enumerate(value['lista'], 1):
                DADOS.append([cont,  str(k.estudante.pessoa.nome), str(k.estudante.pessoa.genero).upper(),  str(k.estudante.pessoa.bi),  str(k.curso.nome), str(k.ano.nome).upper(), str(k.semestre.nome)])
            
            LEGENDA=('#', 'NOME', 'GENERO', 'IDENTIFICAÇÃO', 'CURSO', 'ANO', 'SEMESTRE')
            TABELA = Table([LEGENDA] + DADOS)
            TABELA.setStyle(TableStyle([
                    ('ALIGN',(0,0),(0,0),'CENTER'),
                    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
                    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
                ]
            ))
    else:
        for cont, k in enumerate(value['lista'], 1):
                DADOS.append([cont,  str(k.estudante.pessoa.nome), str(k.estudante.pessoa.genero).upper(),  str(k.estudante.pessoa.bi),  str(k.curso.nome), '__________________________'])
            
        LEGENDA=('#', 'NOME', 'GENERO', 'IDENTIFICAÇÃO', 'CURSO', 'ASSINATURA')
        TABELA = Table([LEGENDA] + DADOS)
        TABELA.setStyle(TableStyle([
                ('ALIGN',(0,0),(0,0),'CENTER'),
                ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
                ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
            ]
        ))

    LISTA.append(TABELA)
    LISTA.append(Spacer(1, 12))

    
    """magName = "Pythonista"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2010"
    freeGift = "tin foil hat"
    full_name = "Marvin Jones"
    address_parts = ["411 State St.", "Reno, NV 80158"]

    for page in range(10):
        # Create return address
        ptext = '<font size=12>%s</font>' % full_name
        LISTA.append(Paragraph(ptext, styles["Normal"]))       
        for part in address_parts:
            ptext = '<font size=12>%s</font>' % part.strip()
            LISTA.append(Paragraph(ptext, styles["Normal"]))

    LISTA.append(Spacer(1, 12))
    ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
    LISTA.append(Paragraph(ptext, styles["Normal"]))
    LISTA.append(Spacer(1, 12))

    ptext = '<font size=12>We would like to welcome you to our subscriber base 
    for %s Magazine! You will receive %s issues at the excellent introductory 
    price of $%s. Please respond by %s to start receiving your subscription 
    and get the following free gift: %s.</font>'
    ptext = ptext % (magName, issueNum, subPrice, limitedDate, freeGift)
    LISTA.append(Paragraph(ptext, styles["Justify"]))
    LISTA.append(Spacer(1, 12))

    ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
    LISTA.append(Paragraph(ptext, styles["Justify"]))
    LISTA.append(Spacer(1, 12))
    ptext = '<font size=12>Sincerely,</font>'
    LISTA.append(Paragraph(ptext, styles["Normal"]))"""
    
    LISTA.append(PageBreak())
    #p.showPage()
    
    
    doc.build(LISTA, onFirstPage=rodape_numero_pagina_imagem_horizontal, onLaterPages=rodape_numero_pagina_imagem_horizontal)
    response.write(buffer.getvalue())
    buffer.close()
    return response
