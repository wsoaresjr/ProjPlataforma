from django.shortcuts import render, redirect, get_object_or_404
from .models import Grupo
from .forms import GrupoForm

# Cadastrar grupo
def cadastrar_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecionar para a página inicial
    else:
        form = GrupoForm()
    return render(request, 'grupos/cadastrar_grupo.html', {'form': form})

# Editar grupo
def editar_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GrupoForm(instance=grupo)
    return render(request, 'grupos/editar_grupo.html', {'form': form, 'grupo': grupo})

# Excluir grupo
def excluir_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        grupo.delete()
        return redirect('home')
    return render(request, 'grupos/excluir_grupo.html', {'grupo': grupo})
