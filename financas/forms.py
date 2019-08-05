from django import forms
from django.forms import ModelForm
from financas.models import Pagamento
from secretaria.models import Pessoa, Estudante, Profissao
from core_help.core import retorna_id




class PagamentoForm(ModelForm):
    estudante = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    class Meta:
        model = Pagamento
        fields = ['grau', 'tipo', 'parecela_mestrado', 'parecela_posgraduacao', 'valor', 'data_pagamento']
        widgets = {
            'grau': forms.Select(attrs={'class': 'form-control ajax_grauPagamento'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'parecela_mestrado': forms.Select(attrs={'class': 'form-control ajax_parecela_mestrado'}),
            'parecela_posgraduacao': forms.Select(attrs={'class': 'form-control ajax_parecela_posgraduacao'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'data_pagamento': forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
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


    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if float(valor) < 0:
            raise forms.ValidationError("O valor não é valida")
        return valor
