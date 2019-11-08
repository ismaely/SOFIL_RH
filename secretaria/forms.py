from django import forms
from django.forms import ModelForm
from core_help.opcoes_escolha import GRAU_ACDAEMICO_DOCENTE, CATEGORIA_UTILIZADOR, GRAU, TIPO_DECLARACAO, TIPO_CONSULTAR_DADOS
from secretaria.models import Pessoa, Estudante,  Profissao, Modulo_Disciplina, Monografia,Matricula, Nota, Cursos, Especialidade, Ano, Nota_final_Monografia
from core_help.core import retorna_id, retorna_id_estudante
#from SOFIL_RH.settings import DATE_FORMAT, DATE_INPUT_FORMATS
from SOFIL_RH import settings

#from django.conf import settings
# forms.py
# @Author : Gunza Ismael (7ilipe@gmail.com)Mon
# @Link   : 
# @Date   : 17/06/2019, 23:41:21


LISTA_CURSOS = [(k.id, k.nome) for k in Cursos.objects.select_related('grau_academico').all()]
LISTA_ESPECIALIDADE = [(k.id, k.nome) for k in Especialidade.objects.select_related('curso').all()]

class PessoaForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    nome_pai = forms.CharField(max_length=100, required=False,  widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    nome_mae = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={ 'class': 'form-control maiuscula'}))
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
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



class EstudanteForm(ModelForm):
    graduado = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    especialidade = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_conclusao = forms.CharField(max_length=90, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    numero_estudante = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nota_final = forms.CharField(max_length=2, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_inscricao = forms.CharField(max_length=90, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
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
    sigla_codigo = forms.CharField(max_length=100,required=False,  widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    horas = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    credito = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(widget=forms.Select(choices = LISTA_MESTRADO , attrs={'class': 'form-control'}))
    #tipo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Modulo_Disciplina
        fields = ['nome', 'sigla_codigo', 'credito', 'ano', 'semestre', 'especialidade', 'estado', 'horas']
        widgets = {
            'ano': forms.Select(attrs={'class': 'form-control ajax_ano'}),
            'semestre': forms.Select(attrs={'class': 'form-control ajax_semestre'}),
            'especialidade': forms.Select(attrs={'class': 'form-control'}),
        }



LISTA_POSGRADUACAO = [(k.id, k.nome) for k in Cursos.objects.select_related('grau_academico').filter(grau_academico_id = 1).all()]
class Modulo_PosGraduacaoForm(ModelForm):
    nome = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sigla_codigo = forms.CharField(max_length=100,required=False,  widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    estado = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(required=False, widget=forms.Select(choices=LISTA_POSGRADUACAO , attrs={'class': 'form-control'}))
    #tipo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Modulo_Disciplina
        fields = ['nome', 'sigla_codigo', 'estado','semestre']
        widgets = {
            'semestre': forms.Select(attrs={'class': 'form-control'}),
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
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'especialidade': forms.Select(attrs={'class': 'form-control'}),
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
    def clean_bi(self):
        bi = self.cleaned_data.get('bi')
        try:
            bix = Pessoa.objects.get(bi=bi)
            if bix.id is not None:
                return bi
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("Nã existe estudante com esse número do B.I")


# formualrio para emitir declaração e para fazer consulta dos dados normal
class Emitir_declaracao_ConsultarDados_Form(forms.Form):
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    motivo_declaracao = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.CharField(required=False, widget=forms.Select(choices = TIPO_DECLARACAO , attrs={'class': 'form-control'}))
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





ANO_LISTA =[]
ANO_LISTA.append(['','-------'])
for ano in Ano.objects.all():
    ANO_LISTA.append([int(ano.id), str(ano.nome)])
class Menu_listagem_Form(forms.Form):
    grau = forms.CharField(widget=forms.Select(choices=GRAU, attrs={'class': 'form-control grau_ajax'}))
    curso = forms.CharField(widget=forms.Select(choices='', attrs={'class': 'form-control grau_curso_ajax ajax_curso_especialidade'}))
    especialidade = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control'}))
    ano = forms.CharField(required=False,widget=forms.Select(choices=ANO_LISTA, attrs={'class': 'form-control ajax_ano'}))
    semestre = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_semestre'}))
    data_entrada = forms.CharField(required=False, max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    
    
class Consultar_alterar_pessoaForm(forms.Form):
    estudante = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))

