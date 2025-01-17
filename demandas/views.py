from django.shortcuts import render, redirect, get_object_or_404
from .models import Demanda, Item
from .forms import DemandaForm, ItemForm
from disciplinas.models import Disciplina
from etapas.models import Etapa
from matrizes.models import Matriz
from usuarios.models import Usuario
from django.db.models import Max

def listar_demandas(request):
    demandas = Demanda.objects.all()
    return render(request, 'demandas/listar_demandas.html', {'demandas': demandas})

def cadastrar_demanda(request):
    if request.method == 'POST':
        demanda_form = DemandaForm(request.POST)
        if demanda_form.is_valid():
            demanda = demanda_form.save()
            return redirect('listar_demandas')
    else:
        demanda_form = DemandaForm()
    return render(request, 'demandas/cadastrar_demanda.html', {'form': demanda_form})


def gerar_itens(request, cod_demanda):
    demanda = get_object_or_404(Demanda, cod_demanda=cod_demanda)
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.demanda = demanda

            # Gerar códigos de itens com a lógica descrita
            ultimo_item = Item.objects.filter(disciplina=item.disciplina, etapa=item.etapa).aggregate(Max('cod_item'))
            proximo_codigo = int(ultimo_item['cod_item__max'][-6:]) + 1 if ultimo_item['cod_item__max'] else 0
            base_cod_item = f"{item.disciplina.sigla}{item.etapa.cod_etapa}"

            for i in range(item.qtd_itens):
                item.cod_item = f"{base_cod_item}{proximo_codigo:06d}"
                proximo_codigo += 1
                item.save()
            return redirect('detalhar_demanda', cod_demanda=demanda.cod_demanda)
    else:
        item_form = ItemForm()

    # Filtrar usuários dos grupos corretos
    elaboradores = Usuario.objects.filter(usuariogrupo__grupo__nome_grupo='Elaboradores').distinct()
    revisores = Usuario.objects.filter(usuariogrupo__grupo__nome_grupo='Revisores').distinct()

    return render(request, 'demandas/gerar_itens.html', {
        'form': item_form,
        'demanda': demanda,
        'elaboradores': elaboradores,
        'revisores': revisores,
    })





def detalhar_demanda(request, cod_demanda):
    demanda = get_object_or_404(Demanda, cod_demanda=cod_demanda)
    itens = demanda.itens.all()
    return render(request, 'demandas/detalhar_demanda.html', {'demanda': demanda, 'itens': itens})



def editar_demanda(request, cod_demanda):
    demanda = get_object_or_404(Demanda, cod_demanda=cod_demanda)
    if request.method == 'POST':
        form = DemandaForm(request.POST, instance=demanda)
        if form.is_valid():
            form.save()
            return redirect('listar_demandas')
    else:
        form = DemandaForm(instance=demanda)
    return render(request, 'demandas/editar_demanda.html', {'form': form, 'demanda': demanda})



def editar_itens(request, cod_demanda):
    demanda = get_object_or_404(Demanda, cod_demanda=cod_demanda)
    itens = demanda.itens.all()

    if request.method == 'POST':
        for item in itens:
            elaborador_id = request.POST.get(f'elaborador_{item.cod_item}')
            revisor_id = request.POST.get(f'revisor_{item.cod_item}')
            if elaborador_id:
                item.elaborador = Usuario.objects.get(pk=elaborador_id)
            if revisor_id:
                item.revisor = Usuario.objects.get(pk=revisor_id)
            item.save()
        return redirect('detalhar_demanda', cod_demanda=cod_demanda)

    # Filtrar usuários dos grupos corretos
    elaboradores = Usuario.objects.filter(usuariogrupo__grupo__nome_grupo='Elaboradores').distinct()
    revisores = Usuario.objects.filter(usuariogrupo__grupo__nome_grupo='Revisores').distinct()

    return render(request, 'demandas/editar_itens.html', {
        'demanda': demanda,
        'itens': itens,
        'elaboradores': elaboradores,
        'revisores': revisores,
    })

