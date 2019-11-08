# forms.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 03/11/2019, 09:11:22
from django import forms
from django.forms import ModelForm
from core_help.opcoes_escolha import GRAU_ACDAEMICO_DOCENTE, CATEGORIA_UTILIZADOR, GRAU, TIPO_DECLARACAO, TIPO_CONSULTAR_DADOS
from secretaria.models import Pessoa, Estudante,  Profissao, Modulo_Disciplina, Monografia,Matricula, Nota, Cursos, Especialidade, Ano, Nota_final_Monografia
from core_help.core import retorna_id, retorna_id_estudante
from core_help.models import Estatistica_Opcao
#from SOFIL_RH.settings import DATE_FORMAT, DATE_INPUT_FORMATS


#LISTA_CURSOS = [(k.id, k.nome) for k in Cursos.objects.select_related('grau_academico').all()]
ESPECIALIDADE= []
ESPECIALIDADE.append(['','-------'])
for k in Especialidade.objects.select_related('curso').all():
    ESPECIALIDADE.append([int(k.id), str(k.nome)])

LISTA_MESTRADO = [(k.id, k.nome) for k in Cursos.objects.select_related('grau_academico').filter(grau_academico_id = 2).all()]
OPCAO = [(k.id, k.nome) for k in Estatistica_Opcao.objects.all()]

ANO_LISTA =[]
ANO_LISTA.append(['','-------'])
for ano in Ano.objects.all():
    ANO_LISTA.append([int(ano.id), str(ano.nome)])

class Estatistica_Mestrado_Form(forms.Form):
    titulo = forms.CharField(max_length=190,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_incial = forms.CharField(max_length=20,required=False,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    data_final = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    ano = forms.CharField(required=False,widget=forms.Select(choices=ANO_LISTA, attrs={'class': 'form-control ajax_ano'}))
    semestre = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_semestre'}))
    curso = forms.CharField(widget=forms.Select(choices = LISTA_MESTRADO , attrs={'class': 'form-control'}))
    especialidade = forms.CharField(required=False, widget=forms.Select(choices = ESPECIALIDADE , attrs={'class': 'form-control'}))
    opcao = forms.CharField(required=False, widget=forms.Select(choices = OPCAO , attrs={'class': 'form-control'}))
    