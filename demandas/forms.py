from django import forms
from .models import Demanda, Item

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['cod_demanda', 'nome_demanda', 'observacoes']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'disciplina', 'etapa', 'matriz', 'padrao_item', 'tipo_item',
            'descritor', 'qtd_itens', 'elaborador', 'data_elaborador',
            'revisor', 'data_revisor'
        ]
