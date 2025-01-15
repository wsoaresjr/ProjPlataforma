from django.shortcuts import render, redirect, get_object_or_404
from .models import Subprograma
from .forms import SubprogramaForm

# Listar subprogramas
def listar_subprogramas(request):
    subprogramas = Subprograma.objects.all()
    return render(request, 'subprogramas/listar_subprogramas.html', {'subprogramas': subprogramas})

# Cadastrar subprograma
def cadastrar_subprograma(request):
    if request.method == 'POST':
        form = SubprogramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_subprogramas')
    else:
        form = SubprogramaForm()
    return render(request, 'subprogramas/cadastrar_subprograma.html', {'form': form})

# Editar subprograma
def editar_subprograma(request, pk):
    subprograma = get_object_or_404(Subprograma, pk=pk)
    if request.method == 'POST':
        form = SubprogramaForm(request.POST, instance=subprograma)
        if form.is_valid():
            form.save()
            return redirect('listar_subprogramas')
    else:
        form = SubprogramaForm(instance=subprograma)
    return render(request, 'subprogramas/editar_subprograma.html', {'form': form, 'subprograma': subprograma})

# Excluir subprograma
def excluir_subprograma(request, pk):
    subprograma = get_object_or_404(Subprograma, pk=pk)
    if request.method == 'POST':
        subprograma.delete()
        return redirect('listar_subprogramas')
    return render(request, 'subprogramas/excluir_subprograma.html', {'subprograma': subprograma})
