from django import forms
from django.forms import ModelForm
from core_help.opcoes_escolha import GRAU_ACDAEMICO_DOCENTE, CATEGORIA_UTILIZADOR, GRAU, TIPO_DECLARACAO, TIPO_CONSULTAR_DADOS
from secretaria.models import (Pessoa, Estudante,  Profissao, Modulo_Disciplina, Monografia,Matricula, Nota, Cursos, Especialidade, Ano, Nota_final_Monografia,
 Chaves_Modulo_Curso)
from core_help.core import retorna_id, retorna_id_estudante
#from SOFIL_RH.settings import DATE_FORMAT, DATE_INPUT_FORMATS
from SOFIL_RH import settings


ANO_LISTA =[]
LISTA_ESPECIALIDADE_2 =[]
RESP = Especialidade.objects.select_related('curso').all()
LISTA_CURSOS = [(k.id, k.nome) for k in Cursos.objects.select_related('grau_academico').all()]
LISTA_ESPECIALIDADE = [(k.id, k.nome) for k in RESP]

LISTA_ESPECIALIDADE_2.append(['','-------'])
for ep in RESP :
    LISTA_ESPECIALIDADE_2.append([int(ep.id), str(ep.nome)])
    
ANO_LISTA.append(['','-------'])
for ano in Ano.objects.all():
    ANO_LISTA.append([int(ano.id), str(ano.nome)])

class PessoaForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    nome_pai = forms.CharField(max_length=100, required=False,  widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    nome_mae = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={ 'class': 'form-control maiuscula'}))
    data_nascimento = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control mask-bi maiuscula'}))
    residencia = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=18, required=False, widget=forms.TextInput(attrs={'class': 'form-control mask-phone'}))
    email = forms.EmailField(max_length=80, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'validate_email'}))
    municipio = forms.CharField(max_length=60, widget=forms.Select(choices="", attrs={'class': 'form-control ajax_municipio'}))
    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_pai', 'nome_mae','genero','data_nascimento', 'bi', 'estado_civil', 'residencia', 'naturalidade', 'telefone', 'email'] 
        widgets = {
            'naturalidade': forms.Select(attrs={'class': 'form-control ajax_naturalidade'}),
            'genero': forms.Select( attrs={'class': 'form-control'}),
            'estado_civil': forms.Select( attrs={'class': 'form-control'}),
        }
        
    def clean_data_nascimento(self):
        try:
            data_nascimento = self.cleaned_data.get('data_nascimento')
            data = []
            data = data_nascimento.split('-')
            total = int(settings.DATA_ANO) - int(data[0])
            if int(total) > 22:
                return data_nascimento
            else:
                raise forms.ValidationError("não é valido a data de nascimento, é menor de idade")
        except Exception as ex:
            raise forms.ValidationError("Erro! Consulta o Admin.. %s" % (ex))
        
       

class EstudanteForm(ModelForm):
    graduado = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    especialidade = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_conclusao = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    numero_estudante = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nota_final = forms.CharField(max_length=2, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_inscricao = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    class Meta:
        model = Estudante
        fields = ['universidade', 'graduado', 'especialidade', 'data_conclusao',  'numero_estudante', 'nota_final', 'data_inscricao'] 
        
        widgets = {
            'universidade': forms.Select(attrs={'class': 'form-control'}),
        }




class ProfissaoForm(ModelForm):
    funcao = forms.CharField(max_length=100,required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    area_profissional = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_experiencia = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    localizacao = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Profissao
        fields = ['instituicao', 'funcao', 'area_profissional', 'ano_experiencia', 'localizacao']
        widgets = {
            'instituicao': forms.TextInput(attrs={'class': 'form-control'}),
        }



LISTA_MESTRADO = [(k.id, k.nome) for k in Cursos.objects.select_related('grau_academico').filter(grau_academico_id = 2).all()]
class Modulo_MestradoForm(ModelForm):
    nome = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #curso = forms.CharField(widget=forms.Select(choices = LISTA_MESTRADO , attrs={'class': 'form-control ajax_modulo_curso_mestrado'}))
    data_entrada = forms.CharField(required=False, max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    class Meta:
        model = Modulo_Disciplina
        fields = ['nome', 'sigla_codigo', 'credito', 'estado','horas']
        widgets = {
            'credito': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla_codigo': forms.TextInput(attrs={'class': 'form-control maiuscula'}),
            'horas': forms.TextInput(attrs={'class': 'form-control'}),
        }



class Chaves_Modulo_Curso_Form(ModelForm):
    curso = forms.CharField(widget=forms.Select(choices = LISTA_MESTRADO , attrs={'class': 'form-control'}))
    class Meta:
        model = Chaves_Modulo_Curso
        fields = ['ano', 'semestre', 'especialidade']
        widgets = {
            'especialidade': forms.Select(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control jax_ano_moduloMestrado ajax_ano'}),
            'semestre': forms.Select(attrs={'class': 'form-control ajax_semestre'}),
        }



LISTA_POSGRADUACAO = [(k.id, k.nome) for k in Cursos.objects.select_related('grau_academico').filter(grau_academico_id = 1).all()]
class Modulo_PosGraduacaoForm(ModelForm):
    nome = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(required=False, widget=forms.Select(choices=LISTA_POSGRADUACAO , attrs={'class': 'form-control'}))
    class Meta:
        model = Modulo_Disciplina
        fields = ['nome', 'sigla_codigo', 'estado']
        widgets = {
            'sigla_codigo': forms.TextInput(attrs={'class': 'form-control maiuscula'}),
            #'semestre': forms.Select(attrs={'class': 'form-control'}),
        }




class MonografiaForm(ModelForm):
    tema = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    estudante = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    docente = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_entrada = forms.CharField(max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    estado = forms.CharField(max_length=8, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    arquivo = forms.FileField()
    class Meta:
        model = Monografia
        fields = ['tema', 'docente', 'data_entrada', 'estado', 'arquivo', 'curso', 'especialidade']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control ajax_curso_monografia'}),
            'especialidade': forms.Select(attrs={'class': 'form-control ajax_especialidade_monografia'}),
        }
    def clean_estudante(self):
        estudante = self.cleaned_data.get('estudante')
        try:
            bi = retorna_id(estudante)
            if bi > 0:
                return estudante
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("O Número do estudante não é valido")



class Matricula_Form(ModelForm):
    estudante = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    ano = forms.CharField(required=False,widget=forms.Select(choices='', attrs={'class': 'form-control ajax_ano'}))
    semestre = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_semestre'}))
    data_matricula= forms.CharField(max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    cadeira_atraso_1 = forms.CharField(required=False, widget=forms.Select(choices="", attrs={'class': 'form-control'}))
    cadeira_atraso_2 = forms.CharField(required=False, widget=forms.Select(choices="", attrs={'class': 'form-control'}))
    cadeira_atraso_3 = forms.CharField(required=False, widget=forms.Select(choices="", attrs={'class': 'form-control'}))
    cadeira_atraso_4 = forms.CharField(required=False, widget=forms.Select(choices="", attrs={'class': 'form-control'}))
    class Meta:
        model = Matricula
        fields = ['curso', 'especialidade', 'data_matricula']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control ajax_curso_especialidade'}),
            'especialidade': forms.Select(attrs={'class': 'form-control ajax_especialidade'}),
        }

    def clean_estudante(self):
        bi = self.cleaned_data.get('estudante')
        try:
            bix = retorna_id(bi)
            if int(bix) > 0:
                return bix
            else:
                raise forms.ValidationError("O Número não é valido")
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("O Número não é valido Não existe")


class Gerar_numeroEstudante_Form(forms.Form):
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control mask-bi maiuscula'}))
    curso = forms.CharField( widget=forms.Select(choices=LISTA_CURSOS, attrs={'class': 'form-control'}))
    def clean_bi(self):
        bi = self.cleaned_data.get('bi')
        try:
            bix = Pessoa.objects.get(bi=bi)
            if bix.id is not None:
                return bi
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("Nã existe estudante com esse número do B.I")


# formualrio para Consulta
class consultar_dados_pessoal_Form(forms.Form):
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    tipo_consulta = forms.CharField(required=False, widget=forms.Select(choices = TIPO_CONSULTAR_DADOS , attrs={'class': 'form-control'}))
    grau = forms.CharField(widget=forms.Select(choices = GRAU , attrs={'class': 'form-control grau_ajax'}))
    curso = forms.CharField(widget=forms.Select(choices='', attrs={'class': 'form-control grau_curso_ajax'}))
    def clean_bi(self):
        bi = self.cleaned_data.get('bi')
        try:
            bix = retorna_id_estudante(bi)
            if int(bix) > 0:
                return bix
            else:
                raise forms.ValidationError("O Número não é valido")
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("O Número não é valido")
        

# formulario emitir declaração
class Emitir_declaracao_ConsultarDados_Form(forms.Form):
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    motivo_declaracao = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.CharField(required=False, widget=forms.Select(choices = TIPO_DECLARACAO , attrs={'class': 'form-control'}))
    grau = forms.CharField(widget=forms.Select(choices = GRAU , attrs={'class': 'form-control grau_ajax'}))
    curso = forms.CharField(widget=forms.Select(choices='', attrs={'class': 'form-control grau_curso_ajax'}))
    def clean_bi(self):
        bi = self.cleaned_data.get('bi')
        try:
            bix = retorna_id_estudante(bi)
            if int(bix) > 0:
                return bix
            else:
                raise forms.ValidationError("O Número não é valido")
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("O Número não é valido")



class Nota_lancamento_Form(ModelForm):
    estudante = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    modulo = forms.CharField(widget=forms.Select(choices='', attrs={'class': 'form-control ajax_modulo'}))
    data_entrada = forms.CharField(max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    curso = forms.CharField( widget=forms.Select(choices=LISTA_CURSOS, attrs={'class': 'form-control ajax_curso'}))
    #ano = forms.CharField(required=False,widget=forms.Select(choices='', attrs={'class': 'form-control ajax_ano'}))
    #semestre = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_semestre'}))
    class Meta:
        model = Nota
        fields = ['nota', 'data_entrada', 'ano', 'semestre']
        widgets = {
            'nota': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control ajax_ano'}),
            'semestre': forms.Select(attrs={'class': 'form-control ajax_semestre'}),
        }

    def clean_estudante(self):
        bi = self.cleaned_data.get('estudante')
        try:
            bix = retorna_id(bi)
            if int(bix) > 0:
                return bix
            else:
                raise forms.ValidationError("O Número não é valido")
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("O Número não é valido Não existe")

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if int(nota) < 0  or int(nota) > 20:
            raise forms.ValidationError("A Nota não é valida")
        return nota




class Nota_final_Monografia_Form(ModelForm):
    estudante = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    data_defesa = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    curso = forms.CharField( widget=forms.Select(choices=LISTA_CURSOS, attrs={'class': 'form-control'}))
    class Meta:
        model = Nota_final_Monografia
        fields = ['nota', 'data_defesa']
        widgets = {
            'nota': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_estudante(self):
        bi = self.cleaned_data.get('estudante')
        try:
            bix = retorna_id(bi)
            if int(bix) > 0:
                return bix
            else:
                raise forms.ValidationError("O Número não é valido")
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("O Número não é valido Não existe")

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if int(nota) < 0  or int(nota) > 20:
            raise forms.ValidationError("A Nota não é valida")
        return nota




class Menu_listagem_Form(forms.Form):
    grau = forms.CharField(widget=forms.Select(choices=GRAU, attrs={'class': 'form-control grau_ajax'}))
    curso = forms.CharField(widget=forms.Select(choices='', attrs={'class': 'form-control grau_curso_ajax ajax_curso_especialidade'}))
    especialidade = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control'}))
    ano = forms.CharField(required=False,widget=forms.Select(choices=ANO_LISTA, attrs={'class': 'form-control ajax_ano'}))
    semestre = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_semestre'}))
    data_entrada = forms.CharField(required=False, max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    



#formulario que vai associar o modulo existente
MODULOS = [(k.id, k.nome) for k in Modulo_Disciplina.objects.select_related().all()]
class Associar_Modulo_Form(forms.Form):
    nome = forms.CharField(widget=forms.Select(choices = MODULOS , attrs={'class': 'form-control'}))
    especialidade = forms.CharField(required=False, widget=forms.Select(choices=LISTA_ESPECIALIDADE_2, attrs={'class': 'form-control'}))
    ano = forms.CharField(required=False,widget=forms.Select(choices=ANO_LISTA, attrs={'class': 'form-control ajax_ano'}))
    semestre = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_semestre'}))
    data_entrada = forms.CharField(required=False, max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    estado = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(widget=forms.Select(choices = LISTA_CURSOS , attrs={'class': 'form-control'}))
    



class Consultar_alterar_pessoaForm(forms.Form):
    estudante = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))

