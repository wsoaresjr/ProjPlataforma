from django import forms
from .models import Descritor

class DescritorForm(forms.ModelForm):
    class Meta:
        model = Descritor
        fields = ['cod_descritor', 'descritor', 'cod_eixo', 'eixo', 'disciplina']
        widgets = {
            'disciplina': forms.Select(attrs={'class': 'form-select'}),  # Lista suspensa
            'descritor': forms.Textarea(attrs={'rows': 4}),  # Área de texto para descritor
        }
