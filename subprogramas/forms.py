from django import forms
from .models import Subprograma

class SubprogramaForm(forms.ModelForm):
    class Meta:
        model = Subprograma
        fields = [
            'cod_subprograma', 'subprograma', 'data_aplicacao', 
            'disciplinas_avaliadas', 'qtd_itens', 'tipo_item', 'padrao_item', 'etapas_avaliadas'
        ]
        widgets = {
            'data_aplicacao': forms.DateInput(attrs={'type': 'date'}),
            'disciplinas_avaliadas': forms.CheckboxSelectMultiple(),
            'etapas_avaliadas': forms.CheckboxSelectMultiple(),
        }
