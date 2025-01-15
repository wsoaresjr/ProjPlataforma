from django.shortcuts import render, redirect, get_object_or_404
from .models import PadraoItem
from .forms import PadraoItemForm

# Listar padrões de item
def listar_padroes_item(request):
    padroes_item = PadraoItem.objects.all()
    return render(request, 'padrao_item/listar_padroes_item.html', {'padroes_item': padroes_item})

# Cadastrar padrão de item
def cadastrar_padrao_item(request):
    if request.method == 'POST':
        form = PadraoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_padroes_item')
    else:
        form = PadraoItemForm()
    return render(request, 'padrao_item/cadastrar_padrao_item.html', {'form': form})

# Editar padrão de item
def editar_padrao_item(request, pk):
    padrao_item = get_object_or_404(PadraoItem, pk=pk)
    if request.method == 'POST':
        form = PadraoItemForm(request.POST, instance=padrao_item)
        if form.is_valid():
            form.save()
            return redirect('listar_padroes_item')
    else:
        form = PadraoItemForm(instance=padrao_item)
    return render(request, 'padrao_item/editar_padrao_item.html', {'form': form, 'padrao_item': padrao_item})

# Excluir padrão de item
def excluir_padrao_item(request, pk):
    padrao_item = get_object_or_404(PadraoItem, pk=pk)
    if request.method == 'POST':
        padrao_item.delete()
        return redirect('listar_padroes_item')
    return render(request, 'padrao_item/excluir_padrao_item.html', {'padrao_item': padrao_item})
