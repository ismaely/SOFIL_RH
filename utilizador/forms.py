#
# forms.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 09/07/2019, 06:10:17
from django import forms
from django.forms import ModelForm
from core_help.opcoes_escolha import CATEGORIA_UTILIZADOR



class Utilizador_Form(forms.Form):
    senha = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nome_utilizador = forms.CharField(max_length=80, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sofia.filipe'}))
    categoria = forms.CharField(max_length=50, widget=forms.Select(choices=CATEGORIA_UTILIZADOR, attrs={'class': 'form-control'}))



class LoginForm(forms.Form):
    senha = forms.CharField(max_length=90, widget=forms.PasswordInput(attrs={'class': 'form-text'}))
    nome_utilizador = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-text'}))



class Troca_SenhaPadrao_Form(forms.Form):
    senha = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirma_senha = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nome_utilizador = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean_senha(self):
        senha =str(self.cleaned_data.get('senha'))
        confirma_senha = str(self.cleaned_data.get('confirma_senha'))
            
        if senha == "cpppgl":
            raise forms.ValidationError("A senha não é valida")
        else:
            print(senha)
            if len(senha) == len(confirma_senha):
                return senha
            
            raise forms.ValidationError("A senha é diferente!")
    