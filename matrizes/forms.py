from django import forms
from .models import Matriz
from subprogramas.models import Subprograma
from descritores.models import Descritor

class MatrizForm(forms.ModelForm):
    class Meta:
        model = Matriz
        fields = ['cod_matriz', 'matriz', 'programa', 'subprograma', 'disciplina', 'descritores', 'etapa']
        widgets = {
            'descritores': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar subprogramas com base no programa selecionado
        if 'programa' in self.data:
            try:
                programa_id = self.data.get('programa')
                self.fields['subprograma'].queryset = Subprograma.objects.filter(programa_id=programa_id)
            except (ValueError, TypeError):
                self.fields['subprograma'].queryset = Subprograma.objects.none()
        elif self.instance.pk:
            self.fields['subprograma'].queryset = self.instance.programa.subprogramas.all()
        else:
            self.fields['subprograma'].queryset = Subprograma.objects.none()

        # Filtrar descritores com base na disciplina selecionada
        if 'disciplina' in self.data:
            try:
                disciplina_id = self.data.get('disciplina')
                self.fields['descritores'].queryset = Descritor.objects.filter(disciplina_id=disciplina_id)
            except (ValueError, TypeError):
                self.fields['descritores'].queryset = Descritor.objects.none()
        elif self.instance.pk:
            self.fields['descritores'].queryset = self.instance.disciplina.descritores.all()
        else:
            self.fields['descritores'].queryset = Descritor.objects.none()
