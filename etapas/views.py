from django.shortcuts import render, redirect, get_object_or_404
from .models import Etapa
from .forms import EtapaForm

# Listar etapas
def listar_etapas(request):
    etapas = Etapa.objects.all()
    return render(request, 'etapas/listar_etapas.html', {'etapas': etapas})

# Cadastrar etapa
def cadastrar_etapa(request):
    if request.method == 'POST':
        form = EtapaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_etapas')
    else:
        form = EtapaForm()
    return render(request, 'etapas/cadastrar_etapa.html', {'form': form})

# Editar etapa
def editar_etapa(request, pk):
    etapa = get_object_or_404(Etapa, pk=pk)
    if request.method == 'POST':
        form = EtapaForm(request.POST, instance=etapa)
        if form.is_valid():
            form.save()
            return redirect('listar_etapas')
    else:
        form = EtapaForm(instance=etapa)
    return render(request, 'etapas/editar_etapa.html', {'form': form, 'etapa': etapa})

# Excluir etapa
def excluir_etapa(request, pk):
    etapa = get_object_or_404(Etapa, pk=pk)
    if request.method == 'POST':
        etapa.delete()
        return redirect('listar_etapas')
    return render(request, 'etapas/excluir_etapa.html', {'etapa': etapa})
