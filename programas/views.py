from django.shortcuts import render, redirect, get_object_or_404
from .models import Programa
from .forms import ProgramaForm

# Listar programas
def listar_programas(request):
    programas = Programa.objects.all()
    return render(request, 'programas/listar_programas.html', {'programas': programas})

# Cadastrar programa
def cadastrar_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_programas')
    else:
        form = ProgramaForm()
    return render(request, 'programas/cadastrar_programa.html', {'form': form})

# Editar programa
def editar_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    if request.method == 'POST':
        form = ProgramaForm(request.POST, request.FILES, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('listar_programas')
    else:
        form = ProgramaForm(instance=programa)
    return render(request, 'programas/editar_programa.html', {'form': form, 'programa': programa})

# Excluir programa
def excluir_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    if request.method == 'POST':
        programa.delete()
        return redirect('listar_programas')
    return render(request, 'programas/excluir_programa.html', {'programa': programa})
