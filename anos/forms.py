from django import forms
from .models import Ano

class AnoForm(forms.ModelForm):
    class Meta:
        model = Ano
        fields = ['cod_ano', 'ano']
