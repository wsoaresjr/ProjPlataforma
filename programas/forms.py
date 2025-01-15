from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'cod_programa', 'programa', 'data_inicio', 'data_fim', 'nome_contato',
            'telefone_contato', 'email_contato', 'qtd_testes', 'contrato_assinado',
            'arquivo_contrato', 'observacoes'
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 5}),
        }
