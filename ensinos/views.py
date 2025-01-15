from django.shortcuts import render, redirect, get_object_or_404
from .models import Ensino
from .forms import EnsinoForm

# Listar ensinos
def listar_ensinos(request):
    ensinos = Ensino.objects.all()
    return render(request, 'ensinos/listar_ensinos.html', {'ensinos': ensinos})

# Cadastrar ensino
def cadastrar_ensino(request):
    if request.method == 'POST':
        form = EnsinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ensinos')
    else:
        form = EnsinoForm()
    return render(request, 'ensinos/cadastrar_ensino.html', {'form': form})

# Editar ensino
def editar_ensino(request, pk):
    ensino = get_object_or_404(Ensino, pk=pk)
    if request.method == 'POST':
        form = EnsinoForm(request.POST, instance=ensino)
        if form.is_valid():
            form.save()
            return redirect('listar_ensinos')
    else:
        form = EnsinoForm(instance=ensino)
    return render(request, 'ensinos/editar_ensino.html', {'form': form, 'ensino': ensino})

# Excluir ensino
def excluir_ensino(request, pk):
    ensino = get_object_or_404(Ensino, pk=pk)
    if request.method == 'POST':
        ensino.delete()
        return redirect('listar_ensinos')
    return render(request, 'ensinos/excluir_ensino.html', {'ensino': ensino})
