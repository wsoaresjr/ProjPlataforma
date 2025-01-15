from django.shortcuts import render, redirect, get_object_or_404
from .models import Descritor
from .forms import DescritorForm

# Listar descritores
def listar_descritores(request):
    descritores = Descritor.objects.all()
    return render(request, 'descritores/listar_descritores.html', {'descritores': descritores})

# Cadastrar descritor
def cadastrar_descritor(request):
    if request.method == 'POST':
        form = DescritorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_descritores')
    else:
        form = DescritorForm()
    return render(request, 'descritores/cadastrar_descritor.html', {'form': form})

# Editar descritor
def editar_descritor(request, pk):
    descritor = get_object_or_404(Descritor, pk=pk)
    if request.method == 'POST':
        form = DescritorForm(request.POST, instance=descritor)
        if form.is_valid():
            form.save()
            return redirect('listar_descritores')
    else:
        form = DescritorForm(instance=descritor)
    return render(request, 'descritores/editar_descritor.html', {'form': form, 'descritor': descritor})

# Excluir descritor
def excluir_descritor(request, pk):
    descritor = get_object_or_404(Descritor, pk=pk)
    if request.method == 'POST':
        descritor.delete()
        return redirect('listar_descritores')
    return render(request, 'descritores/excluir_descritor.html', {'descritor': descritor})
