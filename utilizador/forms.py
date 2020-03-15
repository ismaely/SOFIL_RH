#
# forms.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 09/07/2019, 06:10:17
from django import forms
from django.db.models import Q
from django.forms import ModelForm
from core_help.opcoes_escolha import CATEGORIA_UTILIZADOR
from django.contrib.auth.models import User
import random, json, re
from core_help.core import retorna_id



class Utilizador_Form(forms.Form):
    senha = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nome_utilizador = forms.CharField(max_length=80, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sofia.filipe'}))
    categoria = forms.CharField(max_length=50, widget=forms.Select(choices=CATEGORIA_UTILIZADOR, attrs={'class': 'form-control'}))
    bi_2 = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control mask-bi maiuscula'}))

    def clean_nome_utilizador(self):
        nome_utilizador =str(self.cleaned_data.get('nome_utilizador'))
        id = retorna_id(self.cleaned_data.get('bi_2'))
        try:
            if nome_utilizador.count('.') == 1:
                resp = len(nome_utilizador) - nome_utilizador.find('.')
                if nome_utilizador.find('.') != 2 and resp > 2:
                    nome = User.objects.get(username=nome_utilizador)
                    if nome.username == nome_utilizador:
                        raise forms.ValidationError("O nome já existe...!")
                    else:
                        return nome_utilizador
                else:
                    raise forms.ValidationError("O ponto(.) não é valido nesta posição!")
            else:
                raise forms.ValidationError("O nome de utilizador não é valido, só deve ter um ponto(.)! Exemplo: sofia.filipe")
        except User.DoesNotExist:
            return nome_utilizador
        
        
    
class Actualizar_categoria_Form(forms.Form):
    categoria = forms.CharField(max_length=50, widget=forms.Select(choices=CATEGORIA_UTILIZADOR, attrs={'class': 'form-control'}))



class LoginForm(forms.Form):
    senha = forms.CharField(max_length=90, widget=forms.PasswordInput(attrs={'class': 'form-text'}))
    nome_utilizador = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-text'}))



class Troca_SenhaPadrao_Form(forms.Form):
    senha = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
    confirma_senha = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={'type': 'password','class': 'form-control'}))
    nome_utilizador = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean_confirma_senha(self):
        senha =str(self.cleaned_data.get('senha'))
        confirma_senha = str(self.cleaned_data.get('confirma_senha'))
            
        if senha == "cpppgl" or len(senha) < 4:
            raise forms.ValidationError("A senha não é valida! é fraca")
        else:
            if senha != confirma_senha:
                raise forms.ValidationError("A senha é diferente!")
            return senha