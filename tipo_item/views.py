from django.shortcuts import render, redirect, get_object_or_404
from .models import TipoItem
from .forms import TipoItemForm

# Listar tipos de item
def listar_tipos_item(request):
    tipos_item = TipoItem.objects.all()
    return render(request, 'tipo_item/listar_tipos_item.html', {'tipos_item': tipos_item})

# Cadastrar tipo de item
def cadastrar_tipo_item(request):
    if request.method == 'POST':
        form = TipoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_item')
    else:
        form = TipoItemForm()
    return render(request, 'tipo_item/cadastrar_tipo_item.html', {'form': form})

# Editar tipo de item
def editar_tipo_item(request, pk):
    tipo_item = get_object_or_404(TipoItem, pk=pk)
    if request.method == 'POST':
        form = TipoItemForm(request.POST, instance=tipo_item)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_item')
    else:
        form = TipoItemForm(instance=tipo_item)
    return render(request, 'tipo_item/editar_tipo_item.html', {'form': form, 'tipo_item': tipo_item})

# Excluir tipo de item
def excluir_tipo_item(request, pk):
    tipo_item = get_object_or_404(TipoItem, pk=pk)
    if request.method == 'POST':
        tipo_item.delete()
        return redirect('listar_tipos_item')
    return render(request, 'tipo_item/excluir_tipo_item.html', {'tipo_item': tipo_item})
