from django import forms
from .models import Ensino

class EnsinoForm(forms.ModelForm):
    class Meta:
        model = Ensino
        fields = ['cod_ensino', 'ensino']
