from django import forms
from .models import Disciplina

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['cod_disciplina', 'disciplina', 'sigla', 'area_conhecimento']
