from django import forms
from .models import TipoItem

class TipoItemForm(forms.ModelForm):
    class Meta:
        model = TipoItem
        fields = ['cod_tipo_item', 'tipo_item']
