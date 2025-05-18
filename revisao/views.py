import os
import json
import xml.etree.ElementTree as ET

from django.conf    import settings
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.urls    import reverse

from revisao.models import ItemRevisor


def painel_revisao(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    itens = (
        ItemRevisor.objects
        .filter(revisor_id=usuario_id)
        .exclude(item=None)
    )
    return render(request,
                  'revisao/listar_itens_revisao.html',
                  {'itens_revisor': itens})


def revisar_item(request, cod_item):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    # busca o registro de revisão do item para este usuário
    ir = get_object_or_404(
        ItemRevisor,
        item__cod_item=cod_item,
        revisor_id=usuario_id
    )
    item = ir.item

    # 1) preenche metadados
    metadados = {
        "Código":    item.cod_item,
        "Disciplina": str(item.disciplina) if item.disciplina else '',
        "Etapa":      str(item.etapa)      if item.etapa      else '',
        "Descritor":  str(item.descritor)  if item.descritor  else '',
        "Gabarito":   "",
    }

    # 2) lê o XML
    xml_path = os.path.join(
        settings.BASE_DIR,
        'elaborar_itens', 'xml_storage',
        f"{item.cod_item}.xml"
    )
    conteudo = {
        "enunciado_html":      "",
        "alternativas_html":   [],
        "justificativas_html": [],
    }

    if os.path.exists(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()

        metadados["Gabarito"] = root.findtext('gabarito', '').strip()

        # enunciado + figura
        cj = root.findtext('conteudo', '')
        if cj:
            try:
                p = json.loads(cj)
                conteudo["enunciado_html"] = p.get("html", "")
            except json.JSONDecodeError:
                conteudo["enunciado_html"] = cj

        # alternativas e justificativas
        def to_html(s):
            if not s:
                return ""
            try:
                return json.loads(s).get("html", "")
            except json.JSONDecodeError:
                return s

        for letra in ['a','b','c','d','e']:
            alt = root.findtext(f'alternativa_{letra}', '')
            jus = root.findtext(f'justificativa_{letra}', '')
            conteudo["alternativas_html"].append(to_html(alt))
            conteudo["justificativas_html"].append(to_html(jus))

    # 3) grava o comentário do revisor
    if request.method == "POST":
        txt = request.POST.get('comentario', '').strip()
        ir.comentario = txt
        ir.save()
        # volta para o painel de revisão, não para a mesma página
        return redirect('painel_revisao')

    comentario_atual = ir.comentario or ""

    return render(request, 'revisao/revisar_item.html', {
        'metadados': metadados,
        'conteudo': conteudo,
        'comentario': comentario_atual,
    })
