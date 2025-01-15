from django import forms
from .models import PadraoItem

class PadraoItemForm(forms.ModelForm):
    class Meta:
        model = PadraoItem
        fields = ['cod_padrao_item', 'padrao_item']
