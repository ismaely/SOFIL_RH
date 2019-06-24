from django import forms
from django.forms import ModelForm
from helper.opcoes_escolha import CATEGORIA_ESTUDANTE, SEMESTRE, CATEGORIA_ESTUDANTE
from secretaria.models import Pessoa, Estudante, Modulo, Profissao
# forms.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 17/06/2019, 23:41:21

class PessoaForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome_pai = forms.CharField(max_length=100, required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome_mae = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))
    residencia = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=18, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=80, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'validate_email'}))
    
    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_pai', 'nome_mae','genero','data_nascimento', 'bi', 'estado_civil', 'residencia', 'naturalidade', 'telefone', 'email'] 
        
        widgets = {
            'naturalidade': forms.Select(attrs={'class': 'form-control'}),
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
    instituicao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    funcao = forms.CharField(max_length=100,required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    area_profissional = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_experiencia = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    localizacao = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Profissao
        fields = ['instituicao', 'funcao', 'area_profissional', 'ano_experiencia', 'localizacao'] 
        