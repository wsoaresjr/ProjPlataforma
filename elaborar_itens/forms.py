from django import forms
from .models import ElaboracaoItem

class ElaboracaoItemForm(forms.ModelForm):
    class Meta:
        model = ElaboracaoItem
        fields = [
            'gabarito', 'conteudo', 'comando',
            'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'alternativa_e',
            'justificativa_a', 'justificativa_b', 'justificativa_c', 'justificativa_d', 'justificativa_e',
        ]
