from django.shortcuts import render, get_object_or_404, redirect
from demandas.models import Item
from .models import ElaboracaoItem
from .forms import ElaboracaoItemForm
import os
import xml.etree.ElementTree as ET
from pathlib import Path
from django.conf import settings

# Caminho base para armazenamento dos arquivos XML
XML_FOLDER = Path(settings.BASE_DIR) / 'elaborar_itens' / 'xml_storage'
XML_FOLDER.mkdir(parents=True, exist_ok=True)

def listar_itens(request):
    # Verificar se o usuário está autenticado
    if 'usuario_id' not in request.session:
        return redirect('/')  # Redirecionar para a página de login

    # Obter o usuário autenticado pelo ID na sessão
    usuario_id = request.session['usuario_id']
    itens = Item.objects.filter(elaborador_id=usuario_id, status_item="A Elaborar")

    return render(request, 'elaborar_itens/listar_itens.html', {'itens': itens})

def carregar_de_xml(cod_item):
    """
    Carrega os dados do arquivo XML associado ao código do item.
    """
    caminho = XML_FOLDER / f"{cod_item}.xml"
    if not caminho.exists():
        return {}

    tree = ET.parse(caminho)
    root = tree.getroot()
    dados = {elem.tag: elem.text or "" for elem in root}
    return dados

def salvar_em_xml(cod_item, dados):
    """
    Salva os dados fornecidos em um arquivo XML baseado no código do item.
    """
    caminho = XML_FOLDER / f"{cod_item}.xml"
    root = ET.Element("Item")
    for key, value in dados.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)
    tree.write(caminho, encoding="utf-8", xml_declaration=True)

def elaborar_item(request, cod_item):
    """
    Página de elaboração de itens com suporte para salvar e carregar dados em XML.
    """
    item = get_object_or_404(Item, cod_item=cod_item)

    # Carregar dados do XML, se existirem
    dados_item = {
        "cod_item": item.cod_item,
        "etapa": item.etapa,
        "descritor": item.descritor.descritor,
        "padrao_item": item.padrao_item,
        "data_limite": item.data_elaborador,  # Renomeado para "Data Limite para Entrega"
    }
    dados_xml = carregar_de_xml(cod_item)
    dados_item.update(dados_xml)

    if request.method == "POST":
        form = ElaboracaoItemForm(request.POST)
        if form.is_valid():
            # Extrair dados do formulário
            dados_a_salvar = {
                "gabarito": form.cleaned_data.get("gabarito", ""),
                "conteudo": request.POST.get("conteudo", ""),
                "comando": request.POST.get("comando", ""),
                "alternativa_a": request.POST.get("alternativa_a", ""),
                "alternativa_b": request.POST.get("alternativa_b", ""),
                "alternativa_c": request.POST.get("alternativa_c", ""),
                "alternativa_d": request.POST.get("alternativa_d", ""),
                "alternativa_e": request.POST.get("alternativa_e", ""),
                "justificativa_a": request.POST.get("justificativa_a", ""),
                "justificativa_b": request.POST.get("justificativa_b", ""),
                "justificativa_c": request.POST.get("justificativa_c", ""),
                "justificativa_d": request.POST.get("justificativa_d", ""),
                "justificativa_e": request.POST.get("justificativa_e", ""),
            }

            # Salvar no XML
            salvar_em_xml(cod_item, dados_a_salvar)

            # Verificar se foi clicado "Salvar e Enviar para Revisão"
            if "salvar_enviar" in request.POST:
                item.status_item = "Para Revisão"
                item.save()

            return redirect("listar_itens")

    form = ElaboracaoItemForm(initial=dados_item)
    return render(request, "elaborar_itens/elaborar_item.html", {"form": form, "dados_item": dados_item})

