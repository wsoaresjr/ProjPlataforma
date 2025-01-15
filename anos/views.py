from django.shortcuts import render, redirect, get_object_or_404
from .models import Ano
from .forms import AnoForm

# Listar anos
def listar_anos(request):
    anos = Ano.objects.all()
    return render(request, 'anos/listar_anos.html', {'anos': anos})

# Cadastrar ano
def cadastrar_ano(request):
    if request.method == 'POST':
        form = AnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_anos')
    else:
        form = AnoForm()
    return render(request, 'anos/cadastrar_ano.html', {'form': form})

# Editar ano
def editar_ano(request, pk):
    ano = get_object_or_404(Ano, pk=pk)
    if request.method == 'POST':
        form = AnoForm(request.POST, instance=ano)
        if form.is_valid():
            form.save()
            return redirect('listar_anos')
    else:
        form = AnoForm(instance=ano)
    return render(request, 'anos/editar_ano.html', {'form': form, 'ano': ano})

# Excluir ano
def excluir_ano(request, pk):
    ano = get_object_or_404(Ano, pk=pk)
    if request.method == 'POST':
        ano.delete()
        return redirect('listar_anos')
    return render(request, 'anos/excluir_ano.html', {'ano': ano})
