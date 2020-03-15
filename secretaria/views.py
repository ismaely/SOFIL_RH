from core_help.includes import *
from core_help.core import retorna_id, retorna_id_estudante

from core_help.views_pdf import(logo_pdf, pdf_cabecario, pdf_horizontal_cabeca, rodape_imagem_Vertical, rodape_numero_pagina_imagem_horizontal, gerar_pdf_simples,
rodape_ficha_matricula)
# Create your views here.



@login_required
def home(request):
    context = {}
    return render (request, 'home_centro.html', context)



@login_required
def visualizar_monografia(request, pk):
    
    resp = Monografia.objects.get(id=pk)
    context = {'lista': resp}
    return render (request, 'secretaria/visualizar_monografia.html', context)




#---- ---------ZONA QUE TEM AS FUNÇOES PARA ELIMINAR --------
@login_required
def eliminar_monografia(request, pk):
    if pk > 0:
        lista = Monografia.objects.get(id=pk).delete()
        sweetify.success(request, 'Dados Eliminados com sucesso!....', button='Ok', timer='3100')
        return HttpResponseRedirect(reverse('secretaria:listar-modulos-mestrado'))




# ---------- ZONA DE FUNÇÃO DE CANCELAR E ATIVAR ------------------

@login_required
def ativar_aprovacao_monografia(request, pk):
    if pk > 0:
        resp = Monografia.objects.get(id=pk)
        resp.estado = "Aprovado"
        resp.save()
        sweetify.success(request, 'Aprovado com sucesso', button='Ok', timer='3100')
    return HttpResponseRedirect(reverse('secretaria:home'))



@login_required
def cancelar_monografia(request, pk):
    if pk > 0:
        resp = Monografia.objects.get(id=pk)
        resp.estado = "Cancelado"
        resp.save()
        sweetify.success(request, 'Monografia Cancelado com sucesso', button='Ok', timer='3100')
    return HttpResponseRedirect(reverse('secretaria:home'))



@login_required
def ativar_modulo_mestrado(request, pk):
    if pk > 0:
        lista = Modulo_Disciplina.objects.get(id=pk)
        lista.estado = "Ativado"
        lista.save()
        sweetify.success(request, 'Ativado com sucesso o Modulo!....', button='Ok', timer='3100')
    return HttpResponseRedirect(reverse('secretaria:listar-modulos-mestrado'))


@login_required
def cancelar_modulo_mestrado(request, pk):
    if pk > 0:
        lista = Modulo_Disciplina.objects.get(id=pk)
        lista.estado = "Cancelado"
        lista.save()
        sweetify.success(request, 'Cancelado com sucesso o Modulo!....', button='Ok', timer='3100')
    return HttpResponseRedirect(reverse('secretaria:listar-modulos-mestrado'))



@login_required
def ativar_modulo_posGraduacao(request, pk):
    if pk > 0:
        lista = Modulo_Disciplina.objects.get(id=pk)
        lista.estado = "Ativado"
        lista.save()
        sweetify.success(request, 'Ativado com sucesso o Modulo!....', button='Ok', timer='3100')
    return HttpResponseRedirect(reverse('secretaria:listar-modulos-posgraduacao'))



@login_required
def cancelar_modulo_posGraduacao(request, pk):
    if pk > 0:
        lista = Modulo_Disciplina.objects.get(id=pk)
        lista.estado = "Cancelado"
        lista.save()
        sweetify.success(request, 'Cancelado com sucesso o Modulo!....', button='Ok', timer='3100')
    return HttpResponseRedirect(reverse('secretaria:listar-modulos-posgraduacao'))


# ------------- ZONA DA LISTAGEM  E CONSULTA DOS DADOS --------------


@login_required
def listar_monografias(request):
    form = Menu_listagem_Form(request.POST or None)
    lista =[]
    if request.method == 'POST':
        if form.is_valid():
            curso = int(form.cleaned_data.get('curso'))
            grau = int(form.cleaned_data.get('grau'))
            #ano = form.cleaned_data.get('ano')
            #semestre = form.cleaned_data.get('semestre')
            especialidade = form.cleaned_data.get('especialidade')
            data = str(form.cleaned_data.get('data_entrada'))
            #print(data[:7])
            if grau == 2:
                
                if len(especialidade) > 0 and len(data) > 4:
                    lista = Monografia.objects.select_related('curso').filter(curso_id = curso, especialidade_id=especialidade, data_entrada__contains=data[:7]).all()
                    context = {'lista': lista, 'grau': grau}
                    return render (request, 'secretaria/listar_monografia.html', context)
               
                # BUCAR COM ESPECIALIDADE
                elif len(especialidade) > 0:
                    lista = Monografia.objects.select_related('curso').filter(curso_id = curso, especialidade_id=especialidade).all()
                    context = {'lista': lista, 'grau': grau}
                    return render (request, 'secretaria/listar_monografia.html', context)

                # ANO,
                elif len(data) > 4:
                    lista = Monografia.objects.select_related('curso').filter(curso_id = curso, data_entrada__contains=data[:7]).all()
                    context = {'lista': lista, 'grau': grau}
                    return render (request, 'secretaria/listar_monografia.html', context)

                # APENAS CURSO
                else:
                    lista = Monografia.objects.select_related('curso').filter(curso_id = curso).all()
                    context = {'lista': lista, 'grau': grau}
                    return render (request, 'secretaria/listar_monografia.html', context)
           
           # pos-graduação buscar as monografia
            else:
                if len(data) > 4:
                    lista = Monografia.objects.select_related('curso').filter(curso_id = curso, data_entrada__contains=data[:7]).all()
                    context = {'lista': lista, 'grau': grau}
                    return render (request, 'secretaria/listar_monografia.html', context)
                else:
                    lista = Monografia.objects.select_related('curso').filter(curso_id = curso).all()
                    context = {'lista': lista, 'grau': grau}
                    return render (request, 'secretaria/listar_monografia.html', context)
            
    context = {'form': form}
    return render (request, 'secretaria/menu_listar_monografia.html', context)




@login_required
def listar_modulos_mestrado(request):
    lista =[]
    lista = Chaves_Modulo_Curso.objects.select_related('semestre').filter(curso_id__grau_academico_id=2).all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_modulos_mestrado.html', context)


@login_required
def listar_modulos_posGraduacao(request):
    lista =[]
    lista = Chaves_Modulo_Curso.objects.select_related('semestre').filter(curso_id__grau_academico_id=1).all()
    context = {'lista': lista}
    return render (request, 'secretaria/listar_modulos_posgraduacao.html', context)


#funão que vai selecionar os dados do cadastro pessoal para ser alterado
@login_required
def consultar_dados_cadastro_pessoa(request):
    form = Consultar_alterar_pessoaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            bi = request.POST.get('estudante')
            resp = Profissao.objects.select_related('estudante').filter(Q(estudante__pessoa__bi__contains=bi)| Q(estudante__numero_estudante__contains=bi) )

            return render (request, 'secretaria/resultado_consulta_alterar.html', {'lista': resp})
        
    context = {'form':form}
    return render (request, 'secretaria/consulta_alterar_dados.html', context)



@login_required
def consultar_dados_pessoal(request):
    form = consultar_dados_pessoal_Form(request.POST or None)
    if form.is_valid():
        numero = form.cleaned_data.get('bi')
        grau = form.cleaned_data.get('grau')
        curso = form.cleaned_data.get('curso')
        tipo_consulta = form.cleaned_data.get('tipo_consulta')
        NOTAS =[]
        nome = ""
        cursos = ""
        if tipo_consulta is not None:
            NOTAS = Nota.objects.select_related('estudante').filter(estudante_id=numero, matricula__curso_id =curso)
            # Mestrado ver a nota
            if grau == '2' and tipo_consulta == 'Nota':
                for item in NOTAS:
                    nome = item.estudante.pessoa.nome
                    cursos = item.matricula.curso.nome
                    break
                context = {'notas': NOTAS, 'nome': nome, 'curso': cursos, 'limite': len(NOTAS), 'grau':grau}
                return render (request, 'secretaria/resultado_consulta_nota.html', context)
            
            elif grau == '2' and tipo_consulta == 'Ficha':
                resp = Profissao.objects.get(estudante_id=numero)
                dados = Estudante_Curso.objects.get(estudante_id=numero, curso_id=curso)
                context = {'lista': resp, 'dados': dados, 'notas': NOTAS, 'limite': len(NOTAS), 'grau':grau}
                return render (request, 'secretaria/ficha_pessoal.html', context)
           
            # pos-graduação
            elif grau == '1' and tipo_consulta == 'Ficha':
                resp = Profissao.objects.get(estudante_id=numero)
                dados = Estudante_Curso.objects.get(estudante_id=numero, curso_id=curso)
                context = {'lista': resp, 'dados': dados, 'notas': NOTAS, 'limite': len(NOTAS), 'grau':grau}
                return render (request, 'secretaria/ficha_pessoal.html', context)
            elif grau == '1' and tipo_consulta == 'Nota':
                for item in NOTAS:
                    nome = item.estudante.pessoa.nome
                    cursos = item.matricula.curso.nome
                    break
                context = {'notas': NOTAS, 'nome': nome, 'curso': cursos, 'limite': len(NOTAS), 'grau':grau}
                return render (request, 'secretaria/resultado_consulta_nota.html', context)
        
    context = {'form':form}
    return render (request, 'secretaria/consultar_dados.html', context)



@login_required
def listar_estudantes_matriculados(request):
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
          
            if grau == 2:
                # BUSCAR TUDO 
                if len(ano) > 0 and len(semestre) > 0 and len(especialidade) > 0 and len(data) > 4:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, ano_id=ano, semestre_id=semestre,data_matricula__contains=data[:7]).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)

                # BUCAR COM ANO, SEMESTRE, ESPECIALIDADE
                elif len(ano) > 0 and len(semestre)  > 0 and len(especialidade) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, ano_id=ano, semestre_id=semestre).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)

                # BUCAR COM ANO, SEMESTRE, DATA
                elif len(ano) > 0 and len(semestre)  > 0 and len(data) > 4:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, ano_id=ano, semestre_id=semestre, data_matricula__contains=data[:7]).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)

                # BUCAR COM ANO, SEMESTRE
                elif len(ano) > 0 and len(semestre) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, ano_id=ano, semestre_id=semestre).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)


                # BUCAR COM ESPECIALIDADE, ANO,
                elif len(especialidade) > 0 and len(data) > 4:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, data_matricula__contains=data[:7]).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)

                # BUCAR COM ESPECIALIDADE
                elif len(especialidade) > 0:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)

                # ANO,
                elif len(data) > 4:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__contains=data[:7]).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)

                # APENAS CURSO
                else:
                    DUPLICADO = []
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso)
                    for item in matricula: # REMOVER OS DADOOS DUPLICADO DE UM MESMO ESTUDANTE
                        if len(DUPLICADO) == 0:
                            DUPLICADO.append(item)
                        else:
                            for dup in DUPLICADO:
                                if dup.estudante_id != item.estudante_id and dup.curso_id != item.curso_id:
                                    DUPLICADO.append(item)
                                    
                    context = {'lista': DUPLICADO, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)
           
            else:
                DUPLICADO = []
                if len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__contains=novaData[0]).all()
                    context = {'lista': matricula, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)
                else:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso).all()
                    for item in matricula: # REMOVER OS DADOOS DUPLICADO DE UM MESMO ESTUDANTE
                        if len(DUPLICADO) == 0:
                            DUPLICADO.append(item)
                        else:
                            for dup in DUPLICADO:
                                if dup.estudante_id != item.estudante_id and dup.curso_id != item.curso_id:
                                    DUPLICADO.append(item)
                    context = {'lista': DUPLICADO, 'grau': grau}
                    return render (request, 'secretaria/listar_estudante.html', context)

    context = {'form': form, 'escolha': 1}
    return render (request, 'secretaria/menu_listagem_matricula.html', context)


# ------------- ZONA DA REQUISÇÃO DE AJAX DOS FORMULARIOS --------------

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



def recebe_naturalidade_retorna_municipio_ajax(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.id, k.nome)for k in Municipio.objects.filter(provincia_id=int(id))]
            dados = {
                'muncipios':  lista,
            }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO RETORNO DOS MUNICIPIOS")



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
            modulos = [(k.modulo.id, k.modulo.nome)for k in Chaves_Modulo_Curso.objects.select_related('curso').filter(curso_id=id).all()]
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




# ------------- ZONA DA EDITAR OU ATUALIZAÇÃO DOS DADOS --------------
#função que vai editar os dados de cadastro
@login_required
def editar_registar_cadastro(request, pk):
    resp = Pessoa.objects.get(id=pk)
    resp_2 = Estudante.objects.get(pessoa_id=resp.id)
    resp_3 = Profissao.objects.get(estudante_id=resp_2.id)
    
    form = PessoaForm(request.POST or None, instance=resp)
    form2 = EstudanteForm(request.POST or None, instance=resp_2)
    form3 = ProfissaoForm(request.POST or None, instance=resp_3)
    if request.method == 'POST':
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            pes = form.save(commit=False)
            #pes.municipio_id = form.cleaned_data.get('municipio')
            pessoa = pes.save()
            estudante = form2.save(commit=False)
            estudante.pessoa_id = pes.id
            estudante.save()
            profissao = form3.save(commit=False)
            profissao.estudante_id = estudante.id
            profissao.save()
            sweetify.success(request, 'Dados Atualizado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))
   
    context = {'form':form, 'form2': form2, 'form3': form3, 'pk':resp.id}
    return render (request, 'secretaria/registar_cadastro_estudante.html', context)



#função que vai editar os dados da maricula
@login_required
def editar_confirma_matricula(request, pk):
    resp = Matricula.objects.get(id=pk)
    form = Matricula_Form(request.POST or None,instance=resp, initial={'estudante': resp.estudante.pessoa.bi})
    if request.method == 'POST':
        if form.is_valid() and validar_cadeira_atraso(request):
            novo = form.save(commit=False)
            novo.ano_id = form.cleaned_data.get('ano')
            novo.semestre_id = form.cleaned_data.get('semestre')
            novo.estudante_id = form.cleaned_data.get('estudante')
            
            if form.cleaned_data.get('cadeira_atraso_1') is not None:
                novo.cadeira_atraso_1_id = form.cleaned_data.get('cadeira_atraso_1')
            if form.cleaned_data.get('cadeira_atraso_2') is not None:
                novo.cadeira_atraso_2_id = form.cleaned_data.get('cadeira_atraso_2')
            if form.cleaned_data.get('cadeira_atraso_3') is not None:
                novo.cadeira_atraso_3_id = form.cleaned_data.get('cadeira_atraso_3')
            if form.cleaned_data.get('cadeira_atraso_4') is not None:
                novo.cadeira_atraso_4_id = form.cleaned_data.get('cadeira_atraso_4')
            
            novo.save()
            sweetify.success(request, 'Dados Atualizado com sucesso!....', button='Ok', timer='3100')
            return render (request, 'secretaria/sucesso_atualizar_matricula.html', {'id': resp.id})
    context = {'form':form, 'pk': resp.id}
    return render (request, 'secretaria/registar_confirma_matricula.html', context)




# função que vai editar os dados da monografia
@login_required
def editar_monografias(request, pk):
    try:
        resp = Monografia.objects.get(id=pk)
        form = MonografiaForm(request.POST or None, instance=resp, initial={'estudante': resp.estudante.pessoa.bi})
        if request.method == 'POST':
            #form = MonografiaForm(request.POST, request.FILES)
            if form.is_valid():
                pessoa = form.save(commit=False)
                pessoa.estudante_id = retorna_id(request.POST.get('estudante'))
                pessoa.save()
                sweetify.success(request, 'Dados da Monografia Alterados com sucesso!....', button='Ok', timer='3100')
                return HttpResponseRedirect(reverse('secretaria:home'))
        context = {'form':form, 'resp': resp}
        return render (request, 'secretaria/registar_Monografia.html', context)
    except Exception as e:
        context = {'form':form, 'resp': resp}
        return render (request, 'secretaria/registar_Monografia.html', context)
    


@login_required
def editar_modulo_mestrado(request, pk):
    
    modu = Chaves_Modulo_Curso.objects.get(id=pk)
    modulo = Modulo_Disciplina.objects.get(id=modu.modulo_id)
    form = Modulo_MestradoForm(request.POST or None, instance=modulo)
    form1 = Chaves_Modulo_Curso_Form(request.POST or None, instance=modu)
    if request.method == 'POST':
        if form.is_valid():
            dad = form.save(commit=False)
            dad.save()
            resp1 = form1.save(commit=False)
            #resp1.modulo_id = modu.id
            resp1.curso_id = request.POST.get('curso')
            resp1.save()
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:listar-modulos-mestrado'))

    context = {'form':form,'form1':form1, 'modulo': modu}
    return render (request, 'secretaria/registar_modulo_mestrado.html', context)



@login_required
def editar_modulo_posGraduacao(request, pk):
    modu = Chaves_Modulo_Curso.objects.get(id=pk)
    modulo = Modulo_Disciplina.objects.get(id=modu.modulo_id)
    form = Modulo_PosGraduacaoForm(request.POST or None, instance=modulo, initial={'curso': modu.curso_id})
    if request.method == 'POST':
        if form.is_valid():
            resp = form.save(commit=False)
            resp.save()
            #resp.curso_id = request.POST['curso']
            modu.curso_id  = form.cleaned_data.get('curso')
            modu.save()
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:listar-modulos-posgraduacao'))

    context = {'form':form,'modulo': modu}
    return render (request, 'secretaria/registar_modulo_posgraducao.html', context)




def alterar_nota(request, pk):
    
    NOTA1 = Nota.objects.get(id=pk)
    form = Nota_lancamento_Form(request.POST or None, instance=NOTA1, initial={'estudante': NOTA1.estudante.numero_estudante} )
    if request.method == 'POST':
        if form.is_valid():
            try:
                curso = int(request.POST.get('curso'))
                modulo_curso = int(request.POST.get('modulo'))
                estudante = form.cleaned_data.get('estudante')
                ano = form.cleaned_data.get('ano')
                semestre = form.cleaned_data.get('semestre')

                modu = Chaves_Modulo_Curso.objects.select_related('curso').get(modulo_id = modulo_curso)
                matricula = Matricula.objects.select_related('curso').get(estudante_id=estudante, curso_id= curso, ano_id=ano, semestre_id=semestre)

                if modu.ano_id == matricula.ano_id and modu.semestre_id == matricula.semestre_id and modu.curso_id == matricula.curso_id:
                    try:
                        descricao = Descricao_Nota.objects.get(valor=request.POST.get('nota'))
                        resp = form.save(commit=False)
                        resp.estudante_id = estudante
                        resp.descricao_id = descricao.id
                        resp.modulo_curso_id =modulo_curso
                        #resp.matricula_id = matricula.id
                        resp.save()
                        sweetify.success(request, 'Inserido com Sucesso!..',position ='top-end', button='Ok', timer='4100')
                    except Exception as e:
                        print("erro alterar nota de mestrado")
                else:
                    if modu.curso_id == matricula.curso_id and curso > 0 and curso < 5:
                        try:
                            descricao = Descricao_Nota.objects.get(valor=request.POST.get('nota'))
                            resp = form.save(commit=False)
                            resp.estudante_id = estudante
                            resp.descricao_id = descricao.id
                            resp.modulo_curso_id = modulo_curso
                            #resp.matricula_id = matricula.id
                            resp.save()
                            sweetify.success(request, 'Inserido com Sucesso..!', button='Ok', timer='4100')
                       
                        except Exception as e:
                            print("erro alterar nota de posgraduação")
                    else:
                        sweetify.error(request, 'Não pode ser lançada a nota porque; não fez a inscrição', position ='top-end',   persistent='OK', timer='4100')
            except Matricula.DoesNotExist:
                sweetify.error(request, 'Não pode ser lançada a nota porque, não esta inscrito na cadeira', position ='top-end',   persistent='OK')

    context = {'form':form, 'escolha': 2, 'id': pk}
    return render (request, 'secretaria/registar_lancamento_nota.html', context)




# --------------- ZONA DO CADASTRO E REGITRO DOS DADOS ------------------
#RECEBE O ID DO CURSO E RETORNA  TODOS OS MODULOS DA QUEL CURSO
def recebe_id_curso_ajax(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.modulo.id, k.modulo.nome)for k in Chaves_Modulo_Curso.objects.select_related('curso').filter(curso_id=id).all()]
            dados = {
                'resposta':  lista
            }
        return JsonResponse(dados)
    except ValueError:
        print("ERRO NO CURSO PARA NOTA ")



@login_required
def registar_nota_final_monografia(request):
    form = Nota_final_Monografia_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            estudante = form.cleaned_data.get('estudante')
            curso = form.cleaned_data.get('curso')
            
            if validar_nota_final_monografia(estudante, curso):
                if Nota_final_Monografia.objects.get(estudante_id=estudante, curso_id=curso).exists():
                    sweetify.info(request, 'O estudante já tem nota final registada!..',position ='top-end', button='Ok', timer='4100')
                else:
                    descricao = Descricao_Nota.objects.get(valor=request.POST.get('nota'))
                    resp = form.save(commit=False)
                    resp.estudante_id = estudante
                    resp.curso_id = curso 
                    resp.descricao_id = descricao.id
                    resp.save()
                    sweetify.success(request, 'Inserido com Sucesso a Nota!..',position ='top-end', button='Ok', timer='4100')
                    return render (request, 'home_centro.html', {})
            else:
                sweetify.error(request, 'Não é possivel Registar a nota final, porque não têm todos modulos feitos !..', persistent='OK', timer='3100')
                
    context = {'form':form}
    return render (request, 'secretaria/registar_nota_final_monografia.html', context)


#VIEW QUE VAI REGISTAR O LANÇAMENTO DE NOTA
@login_required
def lancamento_nota(request):
    form = Nota_lancamento_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                curso = int(request.POST.get('curso'))
                modulo_curso = int(request.POST.get('modulo'))
                estudante = form.cleaned_data.get('estudante')
                ano = form.cleaned_data.get('ano')
                semestre = form.cleaned_data.get('semestre')

                modu = Chaves_Modulo_Curso.objects.select_related('curso').get(modulo_id = modulo_curso)
                matricula = Matricula.objects.select_related('curso').get(estudante_id=estudante, curso_id= curso, ano__nome=ano, semestre__nome=semestre)

                if modu.ano_id == matricula.ano_id and modu.semestre_id == matricula.semestre_id and modu.curso_id == matricula.curso_id:
                    try:
                        notas = Nota.objects.get(estudante_id=estudante, modulo_curso__curso_id=curso, modulo_curso__modulo_id=modulo_curso)
                        if notas.nota is not None:
                            sweetify.error(request, 'O estudante já tem Nota nesta cadeira! <br> Contacta o Admin!..', persistent='OK', timer='3100')
                    except Nota.DoesNotExist:
                        descricao = Descricao_Nota.objects.get(valor=request.POST.get('nota'))
                        resp = form.save(commit=False)
                        resp.estudante_id = estudante
                        resp.descricao_id = descricao.id
                        resp.modulo_curso_id =modulo_curso
                        resp.matricula_id = matricula.id
                        resp.save()
                        sweetify.success(request, 'Inserido com Sucesso!..',position ='top-end', button='Ok', timer='4100')
                else:
                    if modu.curso_id == matricula.curso_id and curso > 0 and curso < 3:
                        try:
                            notas = Nota.objects.get(estudante_id=estudante, modulo_curso__curso_id=curso, modulo_curso__modulo_id=modulo_curso)
                            if notas.nota is not None:
                                sweetify.error(request, 'O estudante já tem Nota nesta cadeira! <br> Contacta o Admin..!', persistent='OK', timer='3100')
                        except Nota.DoesNotExist:
                            descricao = Descricao_Nota.objects.get(valor=request.POST.get('nota'))
                            resp = form.save(commit=False)
                            resp.estudante_id = estudante
                            resp.descricao_id = descricao.id
                            resp.modulo_curso_id = modulo_curso
                            resp.matricula_id = matricula.id
                            resp.save()
                            sweetify.success(request, 'Inserido com Sucesso..!', button='Ok', timer='4100')
                    else:
                        sweetify.error(request, 'Não pode ser lançada a nota porque; não fez a inscrição', position ='top-end',   persistent='OK', timer='4100')
            except Matricula.DoesNotExist:
                sweetify.error(request, 'Não pode ser lançada a nota porque, não esta inscrito', position ='top-end',   persistent='OK')

    context = {'form':form}
    return render (request, 'secretaria/registar_lancamento_nota.html', context)



@login_required
def registar_confirma_matricula(request):
    form = Matricula_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and validar_cadeira_atraso(request):
            resp = form.save(commit=False)
            id_estudante = form.cleaned_data.get('estudante')
            resp.estudante_id = id_estudante
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
            
            
            try:
                estu = Estudante.objects.get(id=id_estudante)
                if estu.numero_estudante == '':
                    #sweetify.error(request, 'O Estudante já tem número de Matricula. <br> Se Deseja trocar consulta o Admin!....', persistent='OK', timer='3100')
                    prog = re.compile('.')
                    bs = re.findall(prog, str(estu.pessoa.bi))
                    parte_bi = bs[9:]
                    respo = Gerar_Numero_Matricula.objects.first()
                    xl = int(respo.numero) + 1
                    respo.numero = xl
                    novo_numero = str(xl)
                    respo.save()
                    for k in parte_bi:
                        novo_numero += k
                    estu.numero_estudante = novo_numero
                    estu.save()
                    Estudante_Curso.objects.create(estudante_id= id_estudante, curso_id= request.POST.get('curso'))
                else:
                    respo = Estudante_Curso.objects.get(estudante_id=id_estudante, curso_id=request.POST.get('curso'))
                    if respo.estudante_id is None:
                        Estudante_Curso.objects.create(estudante_id= id_estudante, curso_id= request.POST.get('curso'))
            except Exception as e:
                Estudante_Curso.objects.create(estudante_id= id_estudante, curso_id= request.POST.get('curso'))
            especialidade = 0
            if request.POST.get('especialidade'):
                especialidade = request.POST.get('especialidade')
            sweetify.success(request, 'Confirmação Realizada com sucesso!....', button='Ok', timer='3100')
            return render (request, 'secretaria/sucesso_matricula.html', {'pk': resp.id, 'esp': especialidade })
    context = {'form':form}
    return render (request, 'secretaria/registar_confirma_matricula.html', context)



# VIEW QUE VAI GERAR O NUMERO DO ESTUDANTE 
@login_required
def gerar_numeroEstudante(request):
    form = Gerar_numeroEstudante_Form(request.POST or None)
    if form.is_valid():
        try:
            curso = request.POST.get('curso')
            prog = re.compile('.')
            bs = re.findall(prog, request.POST['bi'])
            parte_bi = bs[9:]
            #retu = retorna_id(request.POST['bi'])
            #print(retu)
            estu = Estudante_Curso.objects.get(estudante__pessoa__bi=request.POST['bi'], curso_id=curso)
            if estu.id and estu.curso_id:
                sweetify.error(request, 'O Estudante já tem número de Matricula. <br> Se Deseja trocar consulta o Admin!....', persistent='OK', timer='3100')
            else:
                num = Estudante.objects.get(pessoa__bi=request.POST['bi'])
                resp = Gerar_Numero_Matricula.objects.first()
                xl = int(resp.numero) + 1
                resp.numero = xl
                novo_numero = str(xl)
                resp.save()
                for k in parte_bi:
                    novo_numero += k
                num.numero_estudante = novo_numero
                num.save()
                Estudante_Curso.objects.create(estudante_id= num.id, curso_id= curso)
                
                sweetify.success(request, 'Número atribuido com sucesso....', persistent='OK', timer='3100')
                context={'dados': estu, 'numero': novo_numero}
                return render (request, 'secretaria/sucesso_numero_estudante.html', context)
        except Exception as e:
            print(e)
   
    context = {'form':form}
    return render (request, 'secretaria/gerar_numero.html', context)




@login_required
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



@login_required
def associar_modulo_existente(request):
    form = Associar_Modulo_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            curso = request.POST.get('curso')
            modulo = request.POST.get('nome')
            especialidade = form.cleaned_data.get('especialidade')
            ano = form.cleaned_data.get('ano')
            semestre = form.cleaned_data.get('semestre')
            Chaves_Modulo_Curso.objects.create(modulo_id=modulo,curso_id=curso,ano_id=ano,especialidade_id=especialidade,semestre_id=semestre)
            sweetify.success(request, 'Modulo Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))
            #return render (request, 'secretaria/registar_modulo_mestrado.html', context)
    context = {'form':form}
    return render (request, 'secretaria/associar_modulo.html', context)
 



@login_required
def registar_modulo_mestrado(request):
    form = Modulo_MestradoForm(request.POST or None)
    form1 = Chaves_Modulo_Curso_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and form1.is_valid():
            modu = form.save(commit=False)
            modu.save()
            resp1 = form1.save(commit=False)
            resp1.modulo_id = modu.id
            resp1.curso_id = request.POST.get('curso')
            resp1.save()
            sweetify.success(request, 'Modulo Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

            #context = {'form':form,'form1':form1}
            #return render (request, 'secretaria/registar_modulo_mestrado.html', context)
    context = {'form':form,'form1':form1}
    return render (request, 'secretaria/registar_modulo_mestrado.html', context)


@login_required
def registar_modulo_posGraduacao(request):
    form = Modulo_PosGraduacaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            modu= form.save(commit=False)
            modu.save()
            Chaves_Modulo_Curso.objects.create(modulo_id=modu.id, curso_id=form.cleaned_data.get('curso'))
            sweetify.success(request, 'Modulo Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form':form}
    return render (request, 'secretaria/registar_modulo_posgraducao.html', context)



#cadastro dos dados pessoal pela primeira vez
@login_required
def registar_cadastro(request):
    form = PessoaForm(request.POST or None)
    form2 = EstudanteForm(request.POST or None)
    form3 = ProfissaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            pes = form.save(commit=False)
            pes.municipio_id = form.cleaned_data.get('municipio')
            pessoa = pes.save()
            estudante = form2.save(commit=False)
            estudante.pessoa_id = pes.id
            estudante.save()
            profissao = form3.save(commit=False)
            profissao.estudante_id = estudante.id
            profissao.save()
            sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))
   
    context = {'form':form, 'form2': form2, 'form3': form3}
    return render (request, 'secretaria/registar_cadastro_estudante.html', context)



# ------------- ZONA DOS PDF  --------------

#função que vai gerar a ficha de matatricula quando a matricula acabar
@login_required
def imprimir_ficha_matricula(request, pk, value):
    resp = Matricula.objects.select_related('estudante').get(id=pk)
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'
    doc = SimpleDocTemplate(buffer,pagesize=letter, alignment=TA_JUSTIFY, rightMargin=38,leftMargin=70,topMargin=135,bottomMargin=75)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify',  alignment=TA_JUSTIFY, fontSize=12.5, fontName="Times-Roman"))
    centro = ParagraphStyle(name='medio', leading = 15, fontName="Times-Roman")
    estilo_linha = ParagraphStyle(name='medio', leading = 10, fontName="Times-Roman")
    
    #print(request.user)
    Story = []
    TABELA = []
    DADOS = []
    DADOS_2 = []
    DADOS_3 = []
    CADEIRAS = []
    ano = []
    ano = str(resp.data_matricula).split('-')
    ptext = """<font size=13.5>  Recibo Nº:  <br/> Confirmação de Matrícula 
    <br/> %s <br/> Ano Lectivo: %s</font>"""
    ptext = ptext % (resp.curso.nome, ano[0])
    #centro.rightIndent = 27
    centro.leftIndent = 6 * cm
    Story.append(Paragraph(ptext, centro))
    
    # A LINHA PRETA
    linha = '______'
    for lin in range(3):
        linha += linha
    ptext = """<font size=20.5>  <b> %s </b> </font>"""
    ptext = ptext % (linha)
    Story.append(Paragraph(ptext, estilo_linha))
    
    Story.append(Spacer(1, 2* cm))
    # tabela 1ª
    LEGENDA = ['NOME', 'Nº ESTUDANTE']
    DADOS.append([str(resp.estudante.pessoa.nome).upper(), str(resp.estudante.numero_estudante).upper()])
    TABELA = Table([LEGENDA] + DADOS,colWidths=[13.3 * cm, 4.8 * cm, 1.0 * cm, 1.0 * cm])
    TABELA.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
    Story.append(TABELA)
    
    # segunda tabela
    LEGENDA = ['B.I. Nº', 'GÉNERO']
    DADOS_2.append([str(resp.estudante.pessoa.bi).upper(), str(resp.estudante.pessoa.genero).upper()])
    TABELA = Table([LEGENDA] + DADOS_2,colWidths=[13.3 * cm, 4.8 * cm, 1.0 * cm, 1.0 * cm])
    TABELA.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
    Story.append(TABELA)
    
    Story.append(Spacer(1, 14.5))
    # 3ª TABELA DOS MODULOS
    LEGENDA = ['MODULOS DO CURSO', 'SIGLA', 'ANO']
    # posgraduação
    if resp.curso_id >= 1 and resp.curso_id < 5:
        for modul in Chaves_Modulo_Curso.objects.select_related('curso').filter(curso_id=resp.curso_id).all():
            DADOS_3.append([str(modul.modulo.nome), str(modul.modulo.sigla_codigo),''])
    #mestrado
    if resp.curso_id >= 5 and resp.curso_id < 7:
        print(value)
        if value:
            for modul in Chaves_Modulo_Curso.objects.select_related('curso').filter(curso_id=resp.curso_id, especialidade_id=value, semestre_id=resp.semestre_id).all():
                DADOS_3.append([str(modul.modulo.nome), str(modul.modulo.sigla_codigo),str( modul.ano.nome)])
        else:
            for modul in Chaves_Modulo_Curso.objects.select_related('curso').filter(curso_id=resp.curso_id, semestre_id=resp.semestre_id).all():
                DADOS_3.append([str(modul.modulo.nome), str(modul.modulo.sigla_codigo),str( modul.ano.nome)])
    
    TABELA = Table([LEGENDA] + DADOS_3,colWidths=[13.3 * cm, 2.5 * cm, 2.3 * cm, 1.0 * cm])
    TABELA.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
    Story.append(TABELA)
    
    # CADEIRAS EM ATRASO
    if resp.cadeira_atraso_1_id is not None:
        CADEIRAS.append([str(resp.cadeira_atraso_1.nome), str(resp.cadeira_atraso_1.sigla_codigo)])
    if resp.cadeira_atraso_2_id is not None:
        CADEIRAS.append([str(resp.cadeira_atraso_2.nome), str(resp.cadeira_atraso_2.sigla_codigo)])
    if resp.cadeira_atraso_3_id is not None:
        CADEIRAS.append([str(resp.cadeira_atraso_3.nome), str(resp.cadeira_atraso_3.sigla_codigo)])
    if resp.cadeira_atraso_4_id is not None:
        CADEIRAS.append([str(resp.cadeira_atraso_4.nome), str(resp.cadeira_atraso_4.sigla_codigo)])
    
    if resp.cadeira_atraso_1_id is not None or resp.cadeira_atraso_2_id is not None or resp.cadeira_atraso_3_id is not None:
        LEGENDA = ['CADEIRAS EM ATRASO', 'SIGLA', 'ANO']
        TABELA  = Table([LEGENDA] + CADEIRAS, colWidths=[13.3 * cm, 2.5 * cm, 2.3 * cm, 1.0 * cm])
        TABELA.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
        Story.append(TABELA)
    
    # DATA DA CRIAÇÃO DA DECLARAÇÃO
    Story.append(Spacer(1, 3.5))
    DATAS = date.today()
    ptext = 'Luanda aos %s de %s de %s'
    ptext = ptext % (DATAS.day, MESES[DATAS.month - 1], DATAS.year)
    #Story.append(Paragraph(ptext, paragrafo_data))
    
    response['Content-Disposition'] = 'inline; filename=FICHA.pdf' # NOME DO FICHEIRO
    Story.append(PageBreak())
    doc.build(Story, onFirstPage=rodape_ficha_matricula)
    response.write(buffer.getvalue())
    buffer.close()
    return response



# DECLARAÇÃO DO TIPO WORD
@login_required
def emitir_delaracao_word(request):
    form = Emitir_declaracao_ConsultarDados_Form(request.POST or None)
    if form.is_valid():
        tipo = int(form.cleaned_data.get('tipo'))
        grau = int(form.cleaned_data.get('grau'))
        id = form.cleaned_data.get('bi')
        cursos = form.cleaned_data.get('curso')
        motivo_declaracao = form.cleaned_data.get('motivo_declaracao')
        
        #inicio da criação do documento
        folha = os.path.join(settings.BASE_DIR, str('docs_font/declaracao/teste.docx'))
        doc = Document(folha)
        styles = doc.styles
        sections = doc.sections

        section = sections[0]
        
        Nome = ""
        Nome_pai = ""
        Nome_mae = ""
        Data_nascimento = ""
        genero = ""
        bi = ""
        Provincia = ""
        municipio = ""
        ficheiro = ""
        curso = ""
        grau_curso = ""
        numero_estudante = ""
        DATA_auxiliar = []
        ESTUDANTE =[]
        ANO_LECTIVO = []
        CONT = 2
        FICHEIRO = ""
        
        
        #DECLARAÇÃO SEM NOTA
        if int(tipo) == 1:
            section.top_margin = Inches(0.5)
            section.left_margin = Inches(1.2)
            section.right_margin = Inches(1.2)
        
            
            NOTAS = Matricula.objects.select_related('estudante').filter(estudante_id=id, curso_id =cursos)
            for ESTUDANTE in NOTAS:
                Nome ="%s" % (ESTUDANTE.estudante.pessoa.nome)
                Nome_pai = str(ESTUDANTE.estudante.pessoa.nome_pai).lower().title()
                Nome_mae = str(ESTUDANTE.estudante.pessoa.nome_mae).lower().title()
                auxiliar  = str(ESTUDANTE.estudante.pessoa.data_nascimento)
                genero  = str(ESTUDANTE.estudante.pessoa.genero)
                bi = str(ESTUDANTE.estudante.pessoa.bi)
                Provincia = str(ESTUDANTE.estudante.pessoa.naturalidade)
                municipio = str(ESTUDANTE.estudante.pessoa.municipio.nome)
                numero_estudante = str(ESTUDANTE.estudante.numero_estudante)
                curso ="%s" % (ESTUDANTE.curso.nome)
                grau_curso ="%s" % (ESTUDANTE.curso.grau_academico.nome)
                DATA_auxiliar = auxiliar.split("-")
                break
            FICHEIRO = "DECLARAÇÃO SEM NOTAS - "+ Nome
            if NOTAS.exists():
                Data_nascimento =  DATA_auxiliar[2] + "/" + DATA_auxiliar[1] + "/" + DATA_auxiliar[0]
                 
                paragraph = doc.add_paragraph()
                run = paragraph.add_run('\nDeclaração\n')
                run.bold = True
                run.font.name = 'Rockwell'
                run.font.size = Pt(18)
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                
                corp = doc.add_paragraph()
                corpo = doc.add_paragraph()
                parag = doc.add_paragraph()
                if genero == 'M':
                    cop = corp.add_run("""\n\tPara todos os efeitos, declaro que """)
                    cop.font.name = 'Times New Roman'
                    cop.font.size = Pt(14.5)
                    grau_cursos = corp.add_run("""%s""" %(Nome))
                    grau_cursos.bold = True
                    grau_cursos.font.name = 'Times New Roman'
                    grau_cursos.font.size = Pt(14.5)
                    cop = corp.add_run(""", filho de %s e de %s, natural de %s, Província de %s, nascido aos %s, portador do B.I. Nº %s, sob processo Nº %s, %s """ % (Nome_pai, Nome_mae, municipio, Provincia, Data_nascimento, bi, numero_estudante,motivo_declaracao))
                    cop.font.name = 'Times New Roman'
                    cop.font.size = Pt(14.5)
                    grau_cursos = corp.add_run("""%s em %s.""" %(grau_curso,curso))
                    grau_cursos.bold = True
                    grau_cursos.font.name = 'Times New Roman'
                    grau_cursos.font.size = Pt(14.5)
                    
                    cop = parag.add_run("""\n\tPor ser verdade, mandei passar a presente declaração, que vai por mim assinada e autenticada com selo branco em uso nesta Instituição.\n\n""")
                    cop.font.name = 'Times New Roman'
                    cop.font.size = Pt(14.5)
                    parag.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                else:
                    cop = corp.add_run("""\n\tPara todos os efeitos, declaro que """)
                    cop.font.name = 'Times New Roman'
                    cop.font.size = Pt(14.5)
                    grau_cursos = corp.add_run("""%s""" %(Nome))
                    grau_cursos.bold = True
                    grau_cursos.font.name = 'Times New Roman'
                    grau_cursos.font.size = Pt(14.5)
                    cop = corp.add_run(""", filha de %s e de %s, natural de %s, Província de %s, nascida aos %s, portadora do B.I. Nº %s, sob processo Nº %s, %s """ % (Nome_pai, Nome_mae, municipio, Provincia, Data_nascimento, bi, numero_estudante,motivo_declaracao))
                    cop.font.name = 'Times New Roman'
                    cop.font.size = Pt(14.5)
                    grau_cursos = corp.add_run("""%s em %s.""" %(grau_curso,curso))
                    grau_cursos.bold = True
                    grau_cursos.font.name = 'Times New Roman'
                    grau_cursos.font.size = Pt(14.5)
                    
                    cop = parag.add_run("""\n\tPor ser verdade, mandei passar a presente declaração, que vai por mim assinada e autenticada com selo branco em uso nesta Instituição.\n\n""")
                    cop.font.name = 'Times New Roman'
                    cop.font.size = Pt(14.5)
                    parag.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                
       
        # COM NOTA
        else:
            #Medidas da folha , altura e largura
            section.top_margin = Inches(0.3)
            section.left_margin = Inches(0.9)
            section.right_margin = Inches(0.5)
            NOTAS = Nota.objects.select_related('estudante').filter(estudante_id=id, modulo_curso__curso_id =cursos)
            for ESTUDANTE in NOTAS:
                Nome ="%s" % (ESTUDANTE.estudante.pessoa.nome)
                Nome_pai = str(ESTUDANTE.estudante.pessoa.nome_pai).lower().title()
                Nome_mae = str(ESTUDANTE.estudante.pessoa.nome_mae).lower().title()
                auxiliar  = str(ESTUDANTE.estudante.pessoa.data_nascimento)
                genero  = str(ESTUDANTE.estudante.pessoa.genero)
                bi = str(ESTUDANTE.estudante.pessoa.bi)
                Provincia = str(ESTUDANTE.estudante.pessoa.naturalidade)
                municipio = str(ESTUDANTE.estudante.pessoa.municipio.nome)
                numero_estudante = str(ESTUDANTE.estudante.numero_estudante)
                curso ="%s" % (ESTUDANTE.matricula.curso.nome)
                grau_curso ="%s" % (ESTUDANTE.matricula.curso.grau_academico.nome)
                DATA_auxiliar = auxiliar.split("-")
                break
            FICHEIRO = "DECLARAÇÃO COM NOTAS - "+Nome
            if NOTAS.exists():
                Data_nascimento =  DATA_auxiliar[2] + "/" + DATA_auxiliar[1] + "/" + DATA_auxiliar[0]
                 
                paragraph = doc.add_paragraph()
                run = paragraph.add_run('%s em %s ' %(grau_curso, curso))
                run.font.name = 'Berlin Sans FB'
                run.font.size = Pt(14)
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = paragraph.add_run('\nDeclaração com Notas Discriminada')
                run.underline = True
                run.font.name = 'Berlin Sans FB'
                run.font.size = Pt(16)
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
                parag = doc.add_paragraph()
                corpo = doc.add_paragraph()
                if genero == 'M':
                    cop = corpo.add_run("""\n\tEm conformidade com o pedido de informção académica constante no requerimento do estudante %s, filho de %s e de %s, natural de %s, Província de %s, nascido aos %s""" % (Nome, Nome_pai, Nome_mae, municipio, Provincia, Data_nascimento))
                    cop.font.name = 'Berlin Sans FB'
                    cop.font.size = Pt(12.5)
                    
                    cop = corpo.add_run(""", portador do B.I. Nº %s, sob processo Nº %s, depois de compulsada a ficha individual, constatou-se o seguinte aproveitamento:""" % (bi, numero_estudante))
                    cop.font.name = 'Berlin Sans FB'
                    cop.font.size = Pt(12.5)
                    corpo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                else:
                    cop = corpo.add_run("""\n\tEm conformidade com o pedido de informção académica constante no requerimento do estudante %s, filha de %s e de %s, natural de %s, Província de %s, nascida aos %s""" % (Nome, Nome_pai, Nome_mae, municipio, Provincia, Data_nascimento))
                    cop.font.name = 'Berlin Sans FB'
                    cop.font.size = Pt(12.5)
                    
                    cop = corpo.add_run(""", portadora do B.I. Nº %s, sob processo Nº %s, depois de compulsada a ficha individual, constatou-se o seguinte aproveitamento:""" % (bi, numero_estudante))
                    cop.font.name = 'Berlin Sans FB'
                    cop.font.size = Pt(12.5)
                    corpo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                    
            corpo = doc.add_paragraph()
            table = doc.add_table(rows=0, cols=4)
            table.autofit = False
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            row=table.add_row().cells
            
            # medias de cadas celula
            table.columns[0].width=Inches(3.9) #disciplina
            table.columns[1].width=Inches(0.6) #nota
            table.columns[2].width=Inches(1.5) #descrição
            table.columns[3].width=Inches(0.8) #ano lectivo
            
            linha= table.rows[0].cells[0].paragraphs[0].add_run('\nDisciplina') 
            linha.font.name ='Berlin Sans FB'
            linha.font.size = Pt(12.5)
            table.rows[0].cells[0].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
            
            linha= table.rows[0].cells[1].paragraphs[0].add_run('\nNota') 
            linha.font.name ='Berlin Sans FB'
            linha.font.size = Pt(12.5)
            table.rows[0].cells[1].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
            
            linha= table.rows[0].cells[3].paragraphs[0].add_run('Ano Lectivo') 
            linha.font.name ='Berlin Sans FB'
            linha.font.size = Pt(12.5)
            table.rows[0].cells[3].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
        
            # MESTRADO DECLAÇÃO
            if grau == 2:
                if NOTAS.filter(semestre_id=1).exists():
                    row=table.add_row().cells
                    linha = table.rows[1]
                    a, b, c, d = linha.cells[:4]
                    a.merge(b)
                    a.merge(c)
                    a.merge(d)
                    linha=table.rows[1].cells[0].paragraphs[0].add_run('1º Semestre') 
                    linha.font.name ='Berlin Sans FB'
                    linha.font.size = Pt(13)
                    table.rows[1].cells[0].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                    for cont, k in enumerate(NOTAS.filter(semestre_id=1), 1):
                        row=table.add_row().cells
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        linha=table.rows[CONT].cells[0].paragraphs[0].add_run(str(k.modulo_curso.modulo.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        
                        linha=table.rows[CONT].cells[1].paragraphs[0].add_run(str(k.nota)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[1].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[2].paragraphs[0].add_run(str(k.descricao.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        #table.rows[CONT].cells[2].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[3].paragraphs[0].add_run(str(ANO_LECTIVO[0])) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[3].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        CONT = CONT +1
                        
                if NOTAS.filter(semestre_id=2).exists():
                    row=table.add_row().cells
                    #CONT = CONT +1
                    linha = table.rows[CONT]
                    a, b, c, d = linha.cells[:4]
                    a.merge(b)
                    a.merge(c)
                    a.merge(d)
                    linha=table.rows[CONT].cells[0].paragraphs[0].add_run('2º Semestre') 
                    linha.font.name ='Berlin Sans FB'
                    linha.font.size = Pt(13)
                    table.rows[CONT].cells[0].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                    CONT = CONT +1
                    for cont, k in enumerate(NOTAS.filter(semestre_id=2), 1):
                        row=table.add_row().cells
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        linha=table.rows[CONT].cells[0].paragraphs[0].add_run(str(k.modulo_curso.modulo.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        
                        linha=table.rows[CONT].cells[1].paragraphs[0].add_run(str(k.nota)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[1].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[2].paragraphs[0].add_run(str(k.descricao.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        #table.rows[CONT].cells[2].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[3].paragraphs[0].add_run(str(ANO_LECTIVO[0])) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[3].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        CONT = CONT +1
                
                if NOTAS.filter(semestre_id=3).exists():
                    row=table.add_row().cells
                    #CONT = CONT +1
                    linha = table.rows[CONT]
                    a, b, c, d = linha.cells[:4]
                    a.merge(b)
                    a.merge(c)
                    a.merge(d)
                    #CONT = CONT +1
                    for cont, k in enumerate(NOTAS.filter(semestre_id=3), 1):
                        if cont == 1:
                            linha=table.rows[CONT].cells[0].paragraphs[0].add_run("3º Semestre – Especialidade: %s" %(k.modulo_curso.especialidade.nome)) 
                            linha.font.name ='Berlin Sans FB'
                            linha.font.size = Pt(13)
                            table.rows[CONT].cells[0].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                            CONT = CONT +1
                        row=table.add_row().cells
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        linha=table.rows[CONT].cells[0].paragraphs[0].add_run(str(k.modulo_curso.modulo.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        
                        linha=table.rows[CONT].cells[1].paragraphs[0].add_run(str(k.nota)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[1].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[2].paragraphs[0].add_run(str(k.descricao.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        #table.rows[CONT].cells[2].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[3].paragraphs[0].add_run(str(ANO_LECTIVO[0])) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[3].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        CONT = CONT +1
            
            #pos-graduação
            else:
                AUXILIAR =[]
                if NOTAS.all().exists():
                    row=table.add_row().cells
                    linha = table.rows[1]
                    a, b, c, d = linha.cells[:4]
                    a.merge(b)
                    a.merge(c)
                    a.merge(d)
                    for cont, k in enumerate(NOTAS.all()[:4], 1):
                        row=table.add_row().cells
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        linha=table.rows[CONT].cells[0].paragraphs[0].add_run(str(k.modulo_curso.modulo.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        
                        linha=table.rows[CONT].cells[1].paragraphs[0].add_run(str(k.nota)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[1].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[2].paragraphs[0].add_run(str(k.descricao.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        #table.rows[CONT].cells[2].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[3].paragraphs[0].add_run(str(ANO_LECTIVO[0])) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[3].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        CONT = CONT +1
                        
                    row=table.add_row().cells
                    linha = table.rows[CONT]
                    a, b, c, d = linha.cells[:4]
                    a.merge(b)
                    a.merge(c)
                    a.merge(d)
                    CONT = CONT +1
                    for cont, k in enumerate(NOTAS.all()[4:], 1):
                        row=table.add_row().cells
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        linha=table.rows[CONT].cells[0].paragraphs[0].add_run(str(k.modulo_curso.modulo.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        
                        linha=table.rows[CONT].cells[1].paragraphs[0].add_run(str(k.nota)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[1].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[2].paragraphs[0].add_run(str(k.descricao.nome)) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        #table.rows[CONT].cells[2].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        
                        linha=table.rows[CONT].cells[3].paragraphs[0].add_run(str(ANO_LECTIVO[0])) 
                        linha.font.name ='Times New Roman'
                        linha.font.size = Pt(12)
                        table.rows[CONT].cells[3].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
                        CONT = CONT +1
                
            parag = doc.add_paragraph()
            zona_final = doc.add_paragraph()
            try:
                NOTA_FINAL = Nota_final_Monografia.objects.select_related('estudante').get(estudante_id=id, curso_id=cursos)
                if NOTA_FINAL.nota is not None:
                    data_ano = str(NOTA_FINAL.data_defesa)
                    data_ano = data_ano.split("-")
                    cop = zona_final.add_run("""Tendo obtido na defesa dissertação a classificação de bom (%s %s) no ano lectivo de %s""" % (NOTA_FINAL.nota, NOTA_FINAL.descricao,  data_ano[0]))
                    cop.font.name = 'Berlin Sans FB'
                    cop.font.size = Pt(12.5)
                    corpo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            except Nota_final_Monografia.DoesNotExist:
                print("")
        
        # DATA DA CRIAÇÃO DA DECLARAÇÃO
        corpo = doc.add_paragraph()
        rodape = doc.add_paragraph()
        DATAS = date.today()
        cop = rodape.add_run("""\n\tLuanda, %s de %s de %s\n""" % (DATAS.day, MESES[DATAS.month - 1], DATAS.year))
        cop.font.name = 'Berlin Sans FB'
        cop.font.size = Pt(12.5)
        corpo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        # RODAPE COM NOME DO DIREITOR
        paragraph = doc.add_paragraph()
        cop = paragraph.add_run("""\n\nO Director do CPPPGL""")
        cop.font.name = 'Berlin Sans FB'
        cop.font.size = Pt(13)
        corpo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        run = paragraph.add_run('\n\n________________________________________\nProf. Carlos Manuel dos Santos Teixeira')
        run.font.name = 'Berlin Sans FB'
        run.font.size = Pt(13)
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = paragraph.add_run('\n(Professor Associado)')
        run.font.name = 'Berlin Sans FB'
        run.font.size = Pt(13)
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # criação do direitorio para salvar o arquivo
        DATAS = date.today()
        pasta ="/home/ismael/Documentos/Declaracao/"
        if not os.path.exists(pasta):
            os.mkdir(pasta)
        doc.save(pasta+str(DATAS)+'-'+FICHEIRO+".docx")
        #os.system("start modelos.docx")
        context = {'form':form,'escolha': 2}
        return render (request, 'secretaria/emitir_declaracao.html', context)
    lista =[]
    context = {'form':form,'escolha': 2}
    return render (request, 'secretaria/emitir_declaracao.html', context)


# função que vai imprmir a declaração onde estamos a mexer muito
@login_required
def emitir_delaracao(request):
    form = Emitir_declaracao_ConsultarDados_Form(request.POST or None)
    if form.is_valid():
        buffer = BytesIO()
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'
        doc = SimpleDocTemplate(buffer,pagesize=letter, alignment=TA_JUSTIFY, rightMargin=38,leftMargin=70,topMargin=135,bottomMargin=75)
        styles = getSampleStyleSheet()
        
        # importar o tipo de letra
        #reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/berlin_1/BRLNSR.TTF')
        pdfmetrics.registerFont(TTFont('berlin-sans', str(settings.BASE_DIR) + '/docs_font/berlin/berlin-sans-fb.ttf'))
        
        styles.add(ParagraphStyle(name='Justify',  alignment=TA_JUSTIFY, fontSize=12.5, fontName="Times-Roman"))
        styles.add(ParagraphStyle(name='normal_espaco',  alignment=TA_JUSTIFY, leading = 14.5, fontSize=12.5, fontName="berlin-sans"))
        
        sem_nota = ParagraphStyle(name='sem_nota',  alignment=TA_JUSTIFY, leading = 15.5, fontSize=13, fontName="Times-Roman")
        sem_nota_0 = ParagraphStyle(name='sem_nota_0',  alignment=TA_JUSTIFY, leading = 15.5, fontName="Times-Roman")
        sem_nota_2 = ParagraphStyle(name='sem_nota_2',  alignment=TA_JUSTIFY, leading = 15.5, fontName="Times-Roman")
        sem_nota_3 = ParagraphStyle(name='sem_nota_3',  alignment=TA_JUSTIFY, leading = 15.5, fontName="Times-Roman")
        paragrafo_data= ParagraphStyle(name='paragrafo_data',  alignment=TA_JUSTIFY, fontSize=14, fontName="Times-Roman")
        
        centro = ParagraphStyle(name='top1',alignment=TA_CENTER, fontSize = 16, fontName="berlin-sans")
        SEM_NOTA = ParagraphStyle(name='top2',alignment=TA_CENTER, fontSize = 20, fontName="Times-Roman")
        ESQUERDA = ParagraphStyle(name='top3',alignment=TA_LEFT, fontSize = 13, fontName="Times-Roman")
        centro_2 = ParagraphStyle(name='medio', fontSize = 12.5, alignment=TA_RIGHT, fontName="berlin-sans")

        tipo = int(form.cleaned_data.get('tipo'))
        grau = int(form.cleaned_data.get('grau'))
        id = form.cleaned_data.get('bi')
        cursos = form.cleaned_data.get('curso')
        motivo_declaracao = form.cleaned_data.get('motivo_declaracao')
        Nome = ""
        Nome_pai = ""
        Nome_mae = ""
        Data_nascimento = ""
        genero = ""
        bi = ""
        Provincia = ""
        municipio = ""
        ficheiro = ""
        curso = ""
        grau_curso = ""
        DATA_auxiliar = []
        ESTUDANTE =[]
        Story = []
        TABELA = []
        DADOS = []
        DADOS_2 = []
        DADOS_3 = []
        ANO_LECTIVO = []
        
        LEGENDA = ['Disciplina', 'Nota', '', 'Ano Lectivo']
        # DECLARAÇÃO SEM NOTA
        if int(tipo) == 1:
            NOTAS = Matricula.objects.select_related('estudante').filter(estudante_id=id, curso_id =cursos)
            for ESTUDANTE in NOTAS:
                Nome = """<font> <b> %s  </b></font>""" % (ESTUDANTE.estudante.pessoa.nome)
                ficheiro = "%s" % (ESTUDANTE.estudante.pessoa.nome)
                Nome_pai = str(ESTUDANTE.estudante.pessoa.nome_pai).lower().title()
                Nome_mae = str(ESTUDANTE.estudante.pessoa.nome_mae).lower().title()
                auxiliar  = str(ESTUDANTE.estudante.pessoa.data_nascimento)
                genero  = str(ESTUDANTE.estudante.pessoa.genero)
                bi = str(ESTUDANTE.estudante.pessoa.bi)
                Provincia = str(ESTUDANTE.estudante.pessoa.naturalidade)
                municipio = str(ESTUDANTE.estudante.pessoa.municipio.nome)
                curso ="%s" % (ESTUDANTE.curso.nome)
                grau_curso ="%s" % (ESTUDANTE.curso.grau_academico.nome)
                DATA_auxiliar = auxiliar.split("-")
                break
            
            if NOTAS.exists():
                Data_nascimento =  DATA_auxiliar[2] + "/" + DATA_auxiliar[1] + "/" + DATA_auxiliar[0]
                Story.append(Spacer(1, 68))
                Story.append(Paragraph("<b>Declaração</b>", SEM_NOTA))
                Story.append(Spacer(1, 40))

                ptext = """<font size=14.5> 
                Para todos os efeitos, declaro que %s,
                </font>"""
                ptext = ptext % (Nome)
                sem_nota_0.rightIndent = 27
                sem_nota_0.leftIndent = 50
                Story.append(Paragraph(ptext, sem_nota_0))
                
                if genero == 'M':
                    ptext = """<font size=14.5> 
                    filho de %s e de %s, natural de %s, Província de %s, nascido aos %s,
                    Portador do B.I. Nº %s, %s do curso de<b><i> %s em %s.</i></b>
                    </font>"""
                else:
                    ptext = """<font size=14.5> 
                    filha de %s e de %s, natural de %s, Província de %s, nascido aos %s,
                    Portadora do B.I. Nº %s, %s do curso de<b><i> %s em %s.</i></b>
                    </font>"""
                
                ptext = ptext % (Nome_pai, Nome_mae, municipio, Provincia, Data_nascimento, bi, motivo_declaracao, grau_curso, curso)
                sem_nota.rightIndent = 27
                sem_nota.leftIndent = 26
                Story.append(Paragraph(ptext, sem_nota))
                Story.append(Spacer(1, 22))
                
                ptext = """<font size=15> 
                Por ser verdadeira, mandei passar a presente declaração, que vai por 
                </font>"""
                sem_nota_2.leftIndent = 50
                #sem_nota_2.rightIndent = 10
                Story.append(Paragraph(ptext, sem_nota_2))
                
                ptext = """<font size=15> 
                assinada e autenticada com selo branco em uso nesta Instituição.
                
                </font>"""
                sem_nota_3.leftIndent = 26
                #sem_nota_2.rightIndent = 10
                Story.append(Paragraph(ptext, sem_nota_3))
                Story.append(Spacer(1, 60))
            
       
        # DECLARAÇÃO COM NOTA
        else:
            NOTAS = Nota.objects.select_related('estudante').filter(estudante_id=id, modulo_curso__curso_id =cursos)
            for ESTUDANTE in NOTAS:
                Nome = """<font> <B> %s  </B></font>""" % (ESTUDANTE.estudante.pessoa.nome)
                ficheiro = "%s" % (ESTUDANTE.estudante.pessoa.nome)
                Nome_pai = str(ESTUDANTE.estudante.pessoa.nome_pai).lower().title()
                Nome_mae = str(ESTUDANTE.estudante.pessoa.nome_mae).lower().title()
                auxiliar  = str(ESTUDANTE.estudante.pessoa.data_nascimento)
                genero  = str(ESTUDANTE.estudante.pessoa.genero)
                bi = str(ESTUDANTE.estudante.pessoa.bi)
                Provincia = str(ESTUDANTE.estudante.pessoa.naturalidade)
                municipio = str(ESTUDANTE.estudante.pessoa.municipio.nome)
                curso ="%s" % (ESTUDANTE.matricula.curso.nome)
                grau_curso ="%s" % (ESTUDANTE.matricula.curso.grau_academico.nome)
                DATA_auxiliar = auxiliar.split("-")
                break
            
            if NOTAS.exists():
                Data_nascimento =  DATA_auxiliar[2] + "/" + DATA_auxiliar[1] + "/" + DATA_auxiliar[0]
                ptext = '<font size=14 >%s em %s </font>' %(grau_curso, curso)
                Story.append(Paragraph(ptext, centro))
                Story.append(Spacer(10*cm, 4.3))
                Story.append(Paragraph("<u>Declaração com Notas Discriminadas</u>", centro))
                Story.append(Spacer(1, 27))
                Story.append(Paragraph("Em conformidade com o pedido de informção académica constante no requerimento do", centro_2))
                Story.append(Spacer(1, 3))
                if genero == 'M':
                    ptext = """<font size=13> 
                    estudante %s, filho de %s e de %s, natural de %s, Província de %s, nascido aos %s,
                    portador do B.I. Nº %s, depois de compulsada a ficha individual, constatou-se o seguinte aproveitamento:
                    </font>"""
                else:
                    ptext = """<font size=13> 
                    estudante %s, filha de %s e de %s, natural de %s, Província de %s, nascido aos %s,
                    portadora do B.I. Nº %s, depois de compulsada a ficha individual, constatou-se o seguinte aproveitamento:
                    </font>"""
                ptext = ptext % (Nome, Nome_pai, Nome_mae, municipio, Provincia, Data_nascimento, bi)
                Story.append(Paragraph(ptext, styles["normal_espaco"]))
                Story.append(Spacer(1, 12.5))

            
            # MESTRADO DECLAÇÃO
            if grau == 2:
                if NOTAS.filter(semestre_id=1).exists():
                    for cont, k in enumerate(NOTAS.filter(semestre_id=1), 1):
                        if cont == 1:
                            DADOS.append([("1º Semestre")])
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        DADOS.append([str(k.modulo_curso.modulo.nome), str(k.nota),  str(k.descricao.nome),  str(ANO_LECTIVO[0])])
                
                    TABELA = Table([LEGENDA] + DADOS,colWidths=[8.7 * cm, 2.1 * cm, 4 * cm,  2.6 * cm])
                    TABELA.setStyle(TableStyle([
                        ('FONTSIZE', (0, 0), (3, 1), 12.5), # fonte do titulo da tabela 
                        ('ALIGN',(0,0),(3,0),'CENTER'),  # a linha o tiulo no centro 
                        ('ALIGN',(1,0),(1,-1),'CENTER'),  # a linha da Nota no centro
                        ('ALIGN',(3,0),(-1,-1),'CENTER'),  # a linha do Ano Lectivo no centro
                        ('GRID', (0, 0), (6, -1), 1,  colors.black),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                        
                        ('FONTSIZE', (0, 1), (3, 1), 13), #fonte da linha do simestre
                        ('SPAN',(0,1),(3,1)), # espaço da juntar apena uma unica linha do semestre
                        ('ALIGN',(0,1),(3,1),'CENTER'), #centro
                        ]
                        ))
                    Story.append(TABELA)
            
                #CONSTRUINDO A SEGUNDA TABELA DO SEGUNDO TIMESTRE
                if NOTAS.filter(semestre_id=2).exists():
                    for cont, k in enumerate(NOTAS.filter(semestre_id=2), 1):
                        if cont == 1:
                            DADOS_2.append([("2º Semestre")])
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        DADOS_2.append([str(k.modulo_curso.modulo.nome), str(k.nota),  str(k.descricao.nome), str(ANO_LECTIVO[0])])
                        
                    TABELA = Table(DADOS_2,colWidths=[8.7* cm, 2.1 * cm, 4 * cm,  2.6 * cm])
                    TABELA.setStyle(TableStyle([
                        ('ALIGN',(0,0),(3,0),'CENTER'),  # a linha o tiulo no centro 
                        ('ALIGN',(1,0),(1,-1),'CENTER'),  # a linha da Nota no centro
                        ('ALIGN',(3,0),(-1,-1),'CENTER'),  # a linha do Ano Lectivo no centro
                        ('GRID', (0, 0), (6, -1), 1,  colors.black),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                        
                        ('FONTSIZE', (0, 0), (3, 0), 13), #fonte da linha do 2-simestre
                        ('SPAN',(0,0),(3,0)), # espaço da juntar apena uma unica linha do semestre
                        ]
                        ))
                    Story.append(TABELA)
            
                #CONSTRUINDO A 3 TºABELA DO 3º TIMESTRE
                if NOTAS.filter(semestre_id=3).exists():
                    for cont, k in enumerate(NOTAS.filter(semestre_id=3), 1):
                        if cont == 1:
                            DADOS_3.append([("3º Semestre – Especialidade: "+ k.matricula.especialidade.nome)])
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        DADOS_3.append([str(k.modulo_curso.modulo.nome), str(k.nota),  str(k.descricao.nome), str(ANO_LECTIVO[0])])
                        
                    TABELA = Table(DADOS_3,colWidths=[8.7 * cm, 2.1 * cm, 4 * cm,  2.6 * cm])
                    TABELA.setStyle(TableStyle([
                        ('ALIGN',(0,0),(3,0),'CENTER'),  # a linha o tiulo no centro 
                        ('ALIGN',(1,0),(1,-1),'CENTER'),  # a linha da Nota no centro
                        ('ALIGN',(3,0),(-1,-1),'CENTER'),  # a linha do Ano Lectivo no centro
                        ('GRID', (0, 0), (6, -1), 1,  colors.black),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                        
                        ('FONTSIZE', (0, 0), (3, 0), 13), #fonte da linha do 2-simestre
                        ('SPAN',(0,0),(3,0)), # espaço da juntar apena uma unica linha do semestre
                        ]
                        ))
                    Story.append(TABELA)
            
            #POS-GRADUAÇÃO COM NOTA - t
            else:
                AUXILIAR =[]
                Story.append(Spacer(1, 11.5))
                #if NOTAS.filter(modulo__semestre_id=1).exists():
                for cont, k in enumerate(NOTAS.all(), 1):
                    if cont < 5:
                        if cont == 1:
                            DADOS.append([(" ")])
                        ANOs = str(k.data_entrada)
                        ANO_LECTIVO = ANOs.split("-")
                        DADOS.append([str(k.modulo_curso.modulo.nome), str(k.nota),  str(k.descricao.nome),  str(ANO_LECTIVO[0])])
                        AUXILIAR.append(k.modulo_curso.modulo.id)
                    
                TABELA = Table([LEGENDA] + DADOS,colWidths=[8.7 * cm, 2.1 * cm, 4 * cm,  2.6 * cm])
                TABELA.setStyle(TableStyle([
                    ('FONTSIZE', (0, 0), (3, 1), 12.5), # fonte do titulo da tabela 
                    ('ALIGN',(0,0),(3,0),'CENTER'),  # a linha o tiulo no centro 
                    ('ALIGN',(1,0),(1,-1),'CENTER'),  # a linha da Nota no centro
                    ('ALIGN',(3,0),(-1,-1),'CENTER'),  # a linha do Ano Lectivo no centro
                    ('GRID', (0, 0), (6, -1), 1,  colors.black),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                    
                    ('FONTSIZE', (0, 1), (3, 1), 13), #fonte da linha do simestre
                    ('SPAN',(0,1),(3,1)), # espaço da juntar apena uma unica linha do semestre
                    ('ALIGN',(0,1),(3,1),'CENTER'), #centro
                    ]
                    ))
                Story.append(TABELA)
            
                #CONSTRUINDO A SEGUNDA TABELA DO SEGUNDO TIMESTRE
                if len(NOTAS) > 4:
                    for cont, k in enumerate(NOTAS.all(), 1):
                        if cont == 1:
                            DADOS_2.append([(" ")])
                        if k.modulo_curso.modulo.id not in AUXILIAR:
                            ANOs = str(k.data_entrada)
                            ANO_LECTIVO = ANOs.split("-")
                            DADOS_2.append([str(k.modulo_curso.modulo.nome), str(k.nota),  str(k.descricao.nome), str(ANO_LECTIVO[0])])

                    TABELA = Table(DADOS_2,colWidths=[8.7* cm, 2.1 * cm, 4 * cm,  2.6 * cm])
                    TABELA.setStyle(TableStyle([
                        #('ALIGN',(0,0),(3,0),'CENTER'),  # a linha o tiulo no centro 
                        ('ALIGN',(1,0),(1,-1),'CENTER'),  # a linha da Nota no centro
                        ('ALIGN',(3,0),(-1,-1),'CENTER'),  # a linha do Ano Lectivo no centro
                        ('GRID', (0, 0), (6, -1), 1,  colors.black),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                        
                       # ('FONTSIZE', (0, 0), (3, 0), 13), #fonte da linha do 2-simestre
                        #('SPAN',(0,0),(3,0)), # espaço da juntar apena uma unica linha do semestre
                        ]
                        ))
                    Story.append(TABELA)
                    Story.append(Spacer(1, 20))
            
            # DESCRIÇÃO DA NOTA DA DEFESA FINAL
            Story.append(Spacer(1, 4))
            try:
                NOTA_FINAL = Nota_final_Monografia.objects.select_related('estudante').get(estudante_id=id, curso_id=cursos)
                if NOTA_FINAL.nota is not None:
                    data_ano = str(NOTA_FINAL.data_defesa)
                    data_ano = data_ano.split("-")
                    ptext = '<font size=12> Tendo obtido na defesa dissertação a classificação de bom ( %s %s) no ano lectivo de %s </font>'
                    ptext = ptext % (NOTA_FINAL.nota, str(NOTA_FINAL.descricao),  data_ano[0])
                    Story.append(Paragraph(ptext, ESQUERDA))
            except Nota_final_Monografia.DoesNotExist:
                print("")
        
        # DATA DA CRIAÇÃO DA DECLARAÇÃO
        Story.append(Spacer(1, 3.5))
        DATAS = date.today()
        ptext = 'Luanda, %s de %s de %s'
        ptext = ptext % (DATAS.day, MESES[DATAS.month - 1], DATAS.year)
        paragrafo_data.leftIndent = 50
        Story.append(Paragraph(ptext, paragrafo_data))
        
        response['Content-Disposition'] = 'inline; filename='+ficheiro+'.pdf' # NOME DO FICHEIRO
        #RODAPE DA DECLARAÇÃO
        Story.append(PageBreak())
        doc.build(Story, onFirstPage=rodape_imagem_Vertical, onLaterPages=rodape_imagem_Vertical)
        response.write(buffer.getvalue())
        buffer.close()
        #print(response['Content-Disposition'].split("="))
        return response

    lista =[]
    context = {'form':form, 'escolha': 1, 'lista': lista}
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
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, ano_id=ano, semestre_id=semestre,data_matricula__contains=novaData[0]).all()
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
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, ano_id=ano, semestre_id=semestre, data_matricula__contains=novaData[0]).all()
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
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, especialidade_id=especialidade, data_matricula__contains=novaData[0]).all()
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
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__contains=novaData[0]).all()
                    context = {'lista': matricula}
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

                # APENAS CURSO
                else:
                    DUPLICADO = []
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso)
                    for item in matricula: # REMOVER OS DADOOS DUPLICADO DE UM MESMO ESTUDANTE
                        if len(DUPLICADO) == 0:
                            DUPLICADO.append(item)
                        else:
                            for dup in DUPLICADO:
                                if dup.estudante_id != item.estudante_id and dup.curso_id != item.curso_id:
                                    DUPLICADO.append(item)
                    dados = {
                        'lista':  DUPLICADO,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)
                
            else:
                DUPLICADO = []
                #pos-graduação
                if curso > 0 and len(data) > 4:
                    novaData = data.split('-')
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso, data_matricula__contains=novaData[0]).all()
                    dados = {
                        'lista':  matricula,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)
                else:
                    matricula = Matricula.objects.select_related('curso').filter(curso_id=curso).all()
                    for item in matricula: # REMOVER OS DADOOS DUPLICADO DE UM MESMO ESTUDANTE
                        if len(DUPLICADO) == 0:
                            DUPLICADO.append(item)
                        else:
                            for dup in DUPLICADO:
                                if dup.estudante_id != item.estudante_id and dup.curso_id != item.curso_id:
                                    DUPLICADO.append(item)
                    dados = {
                        'lista':  DUPLICADO,
                        'grau': grau,
                        'esp': especialidade
                    }
                    return gerar_pdf_simples(dados)

    context = {'form': form, 'escolha': 2}
    return render (request, 'secretaria/menu_listagem_matricula.html', context)