from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)



from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cod_usuario', 'nome', 'username', 'senha', 'cpf', 'email', 'chave_pix', 'status_ativo']
        widgets = {
            'senha': forms.PasswordInput(),
        }
