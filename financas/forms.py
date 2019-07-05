from django import forms
from django.forms import ModelForm
from financas.models import Pagamento
from secretaria.models import Pessoa, Estudante, Profissao




class PagamentoForm(ModelForm):
    estudante = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_pagamento = forms.CharField(max_length=10,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    valor = forms.CharField(max_length=9, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Pagamento
        fields = ['valor', 'data_pagamento', 'semestre', 'grau_pagamento']
        widgets = {
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'grau_pagamento': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def clean_estudante(self):
        estudante = self.cleaned_data.get('estudante')
        try:
            bi = Pessoa.objects.get(bi=estudante)
            if bi.id is not None:
                return estudante
        except Pessoa.DoesNotExist:
            raise forms.ValidationError("o Numero do estudante não é valido")