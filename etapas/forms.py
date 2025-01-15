from django import forms
from .models import Etapa

class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = ['cod_etapa', 'etapa', 'ensino']
        widgets = {
            'ensino': forms.Select(attrs={'class': 'form-select'}),  # Lista suspensa com Bootstrap
        }
