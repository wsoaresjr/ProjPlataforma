from django.shortcuts import render, redirect, get_object_or_404
from .models import Disciplina
from .forms import DisciplinaForm

# Listar disciplinas
def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas/listar_disciplinas.html', {'disciplinas': disciplinas})

# Cadastrar disciplina
def cadastrar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'disciplinas/cadastrar_disciplina.html', {'form': form})

# Editar disciplina
def editar_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'disciplinas/editar_disciplina.html', {'form': form, 'disciplina': disciplina})

# Excluir disciplina
def excluir_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('listar_disciplinas')
    return render(request, 'disciplinas/excluir_disciplina.html', {'disciplina': disciplina})
