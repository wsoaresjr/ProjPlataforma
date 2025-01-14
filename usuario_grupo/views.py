from django.shortcuts import render, redirect, get_object_or_404
from .models import UsuarioGrupo
from .forms import UsuarioGrupoForm

# Associar usuário a grupo
def associar_usuario_grupo(request):
    if request.method == 'POST':
        form = UsuarioGrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecionar para a página inicial
    else:
        form = UsuarioGrupoForm()
    return render(request, 'usuario_grupo/associar_usuario_grupo.html', {'form': form})

# Editar associação
def editar_associacao(request, pk):
    associacao = get_object_or_404(UsuarioGrupo, pk=pk)
    if request.method == 'POST':
        form = UsuarioGrupoForm(request.POST, instance=associacao)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioGrupoForm(instance=associacao)
    return render(request, 'usuario_grupo/editar_associacao.html', {'form': form, 'associacao': associacao})

# Excluir associação
def excluir_associacao(request, pk):
    associacao = get_object_or_404(UsuarioGrupo, pk=pk)
    if request.method == 'POST':
        associacao.delete()
        return redirect('home')
    return render(request, 'usuario_grupo/excluir_associacao.html', {'associacao': associacao})
