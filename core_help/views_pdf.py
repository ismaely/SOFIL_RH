# views_pdf.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 29/07/2019, 17:23:33
from core_help.includes import *

import pyqrcode


def codigo_qr():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
    )
    data = 'cpppgl-uan'
    qr.add_data(data)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    return img.save('static/codigo_qr/t5.png')


def rodape_factura(canvas, doc):
    # logo da fau
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
    canvas.drawImage(logo, 0, 15, width=580, height=764, mask=None)
    #linha
    canvas.line(60,640,570,640)
    canvas.setFont('Times-Roman',12)
    #caixa da factura
    caixa1 = os.path.join(settings.MEDIA_ROOT, str('logo/caixa3.png'))
    canvas.drawImage(caixa1, 299.5, 518, width=280, height=119, mask=None)
    canvas.drawString(330,642.2,'FACTURA Nº: 2019/000000001')
    canvas.drawString(11.2*cm, 21.5* cm,'Universidade Agostinho Neto')
    canvas.drawString(11.2*cm, 21* cm,'Entidade: CPPPGL')
    canvas.drawString(11.2*cm, 20.5* cm,'Av. Ho Chi Min, Faculdade de Direito')
    canvas.drawString(11.2*cm, 20* cm,'2º Piso - Sala: 4')
    canvas.drawString(11.2*cm, 19.5* cm,'E-mail: cpppgl.org@gmail.com')
    canvas.drawString(11.2*cm, 19* cm,'Telefone: 222-153555')
    canvas.drawString(13.9*cm, 18.3* cm,'Luanda - Angola')
    canvas.drawString(14.3*cm, 17.8* cm,'Data')

    #ASSINATURA
    canvas.line(350,130,570,130)
    canvas.drawString(12.5*cm, 4.2* cm,'O Funcionario:')


    #INFORMAÇÃO EXTRA
    canvas.drawString(2*cm, 5.8* cm,'Nº de Contribuite: 7416013488')
    canvas.drawString(2*cm, 5.3* cm,'Banco Fomento Angola (BFA)')
    canvas.drawString(2*cm, 4.8* cm,'Nº Conta: 140490956.30.001')
    canvas.drawString(2*cm, 4.3* cm,'IBAN-A0 06000600004049095630110')

    #codigo qr
    canvas.drawImage(codigo_qr(), 495, 26, width=73, height=70, mask=None)

    page_num = canvas.getPageNumber()
    #text = "Pagina #%s" % page_num
 

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
 

#RODAPE DA DECLARAÇÃO
def rodape_imagem_Vertical(canvas, doc):
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
    canvas.drawImage(logo, 0, 15, width=580, height=769, mask=None)
    styles = getSampleStyleSheet()
    
    canvas.drawString(269,39*mm,'O Director')
    canvas.line(188,32*mm,406,32*mm)
    canvas.drawString(189,28*mm,'Prof. Carlos Manuel dos Santos Teixeira')
    canvas.drawString(245,23*mm,'(Professor Associado)')
    
    page_num = canvas.getPageNumber()
    

# RODAPE QUE PRECHE A FICHA DE MATRICULA EM PDF
def rodape_ficha_matricula(canvas, doc):
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/ficha_inscricao.png'))
    canvas.drawImage(logo, 0, 15, width=580, height=769, mask=None)
    
    
    
    canvas.drawString(269,39*mm,'Operador')
    canvas.line(188,32*mm,406,32*mm)
    #canvas.drawString(189,28*mm,'Prof. Carlos Manuel dos Santos Teixeira')
    #canvas.drawString(245,23*mm,'(Professor Associado)')
    canvas.drawImage(codigo_qr(), 495, 26, width=73, height=70, mask=None)
    page_num = canvas.getPageNumber()
    #text = "Pagina #%s" % page_num
    #canvas.drawRightString(200*mm, 20*mm, text)


def rodape_numero_pagina_imagem_horizontal(canvas, doc):
    canvas.setPageSize((10.9*inch, 7.7*inch))
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
    canvas.drawImage(logo, 0, 15, width=555, height=534, mask=None)
    page_num = canvas.getPageNumber()
    text = "Pagina #%s" % page_num
    canvas.drawRightString(256*mm, 20*mm, text)



def gerar_pdf_simples(value):
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Lista_Nominal.pdf"'
    #p = canvas.Canvas(buffer)
    doc = SimpleDocTemplate(buffer,pagesize=letter, rightMargin=-120,leftMargin=60,topMargin=340,bottomMargin=75)
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

    #MESTRADO LISTA PDF
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
                DADOS.append([cont, str(k.estudante.pessoa.nome), str(k.estudante.pessoa.genero).upper(),  str(k.estudante.pessoa.bi),  str(k.curso.nome), str(k.ano.nome).upper()])
            
            LEGENDA=('#', 'NOME', 'GENERO', 'IDENTIFICAÇÃO', 'CURSO', 'ANO')
            TABELA = Table([LEGENDA] + DADOS)
            TABELA.setStyle(TableStyle([
                    ('ALIGN',(0,0),(0,0),'CENTER'),
                    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
                    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ('VALIGN',(0,1),(2,1),'MIDDLE')
                ]
            ))

    # POS-GRADUAÇÃO LISTA PDF
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
    LISTA.append(PageBreak())
    #p.showPage()
    
    doc.build(LISTA, onFirstPage=rodape_numero_pagina_imagem_horizontal, onLaterPages=rodape_numero_pagina_imagem_horizontal)
    response.write(buffer.getvalue())
    buffer.close()
    return response
