from django import forms
from usuario_grupo.models import UsuarioGrupo
from usuarios.models import Usuario
from grupos.models import Grupo

class UsuarioGrupoForm(forms.ModelForm):
    class Meta:
        model = UsuarioGrupo
        fields = ['usuario', 'grupo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = Usuario.objects.all()
        self.fields['grupo'].queryset = Grupo.objects.all()
