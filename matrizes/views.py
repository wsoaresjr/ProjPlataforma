from django.shortcuts import render, redirect, get_object_or_404
from .models import Matriz
from .forms import MatrizForm

# Listar matrizes
def listar_matrizes(request):
    matrizes = Matriz.objects.all()
    return render(request, 'matrizes/listar_matrizes.html', {'matrizes': matrizes})

# Cadastrar matriz
def cadastrar_matriz(request):
    if request.method == 'POST':
        form = MatrizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_matrizes')
    else:
        form = MatrizForm()

    return render(request, 'matrizes/cadastrar_matriz.html', {'form': form})

# Editar matriz
def editar_matriz(request, pk):
    matriz = get_object_or_404(Matriz, pk=pk)
    if request.method == 'POST':
        form = MatrizForm(request.POST, instance=matriz)
        if form.is_valid():
            form.save()
            return redirect('listar_matrizes')
    else:
        form = MatrizForm(instance=matriz)
    return render(request, 'matrizes/editar_matriz.html', {'form': form, 'matriz': matriz})

# Excluir matriz
def excluir_matriz(request, pk):
    matriz = get_object_or_404(Matriz, pk=pk)
    if request.method == 'POST':
        matriz.delete()
        return redirect('listar_matrizes')
    return render(request, 'matrizes/excluir_matriz.html', {'matriz': matriz})

# Visualizar conteúdo da matriz
def visualizar_matriz(request, pk):
    matriz = get_object_or_404(Matriz, pk=pk)
    descritores = matriz.descritores.all()
    return render(request, 'matrizes/visualizar_matriz.html', {'matriz': matriz, 'descritores': descritores})



from django.http import JsonResponse
from django.template.loader import render_to_string
from subprogramas.models import Subprograma
from descritores.models import Descritor

def filtrar_subprogramas(request):
    programa_id = request.GET.get('programa')
    subprogramas = Subprograma.objects.filter(programa_id=programa_id)
    html = render_to_string('matrizes/subprograma_dropdown_list_options.html', {'subprogramas': subprogramas})
    return JsonResponse(html, safe=False)

def filtrar_descritores(request):
    disciplina_id = request.GET.get('disciplina')
    descritores = Descritor.objects.filter(disciplina_id=disciplina_id)
    html = render_to_string('matrizes/descritor_checkbox_list.html', {'descritores': descritores})
    return JsonResponse(html, safe=False)


from django.shortcuts import render, get_object_or_404
from .models import Matriz

def ver_matriz(request, cod_matriz):
    matriz = get_object_or_404(Matriz, cod_matriz=cod_matriz)
    descritores = matriz.descritores.all()  # Obter os descritores associados à matriz

    return render(request, 'matrizes/ver_matriz.html', {
        'matriz': matriz,
        'descritores': descritores,
    })


import openpyxl
from django.http import HttpResponse
from .models import Matriz

def exportar_matriz_excel(request, cod_matriz):
    matriz = Matriz.objects.get(cod_matriz=cod_matriz)
    descritores = matriz.descritores.all()

    # Criar o workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matriz"

    # Adicionar cabeçalhos
    ws.append(["Programa", "Subprograma", "Matriz", "Disciplina", "Etapa"])
    ws.append([matriz.programa.programa, matriz.subprograma.subprograma, matriz.matriz, matriz.disciplina.disciplina, matriz.etapa.etapa])

    # Adicionar descritores
    ws.append([])
    ws.append(["Código do Descritor", "Descritor", "Eixo"])
    for descritor in descritores:
        ws.append([descritor.cod_descritor, descritor.descritor, descritor.eixo])

    # Retornar o arquivo Excel
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="Matriz_{cod_matriz}.xlsx"'
    wb.save(response)
    return response



from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def exportar_matriz_pdf(request, cod_matriz):
    matriz = Matriz.objects.get(cod_matriz=cod_matriz)
    descritores = matriz.descritores.all()

    # Configurar tamanho de página e margens
    page_width, page_height = A4
    margin_left = 2 * cm
    margin_top = page_height - 2 * cm
    line_height = 0.5 * cm  # Altura mínima entre linhas

    # Configurar largura das colunas
    col_cod_descritor = 4 * cm
    col_descritor = 10 * cm
    col_eixo = 4 * cm

    # Criar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Matriz_{cod_matriz}.pdf"'

    # Configurar o canvas
    p = canvas.Canvas(response, pagesize=A4)

    # **Destacar os nomes dos campos em negrito**
    def draw_bold_text(x, y, label, value):
        p.setFont("Helvetica-Bold", 10)
        p.drawString(x, y, label)
        p.setFont("Helvetica", 10)
        p.drawString(x + 3.5 * cm, y, value)

    # Inserir informações principais da matriz com negrito
    y_position = margin_top
    draw_bold_text(margin_left, y_position, "Programa:", matriz.programa.programa)
    y_position -= line_height
    draw_bold_text(margin_left, y_position, "Subprograma:", matriz.subprograma.subprograma)
    y_position -= line_height
    draw_bold_text(margin_left, y_position, "Matriz:", matriz.matriz)
    y_position -= line_height
    draw_bold_text(margin_left, y_position, "Disciplina:", matriz.disciplina.disciplina)
    y_position -= line_height
    draw_bold_text(margin_left, y_position, "Etapa:", matriz.etapa.etapa)
    y_position -= 2 * line_height

    # Adicionar cabeçalho da tabela com bordas
    p.setFont("Helvetica-Bold", 10)
    p.rect(margin_left, y_position - line_height, col_cod_descritor, line_height, stroke=1, fill=0)
    p.rect(margin_left + col_cod_descritor, y_position - line_height, col_descritor, line_height, stroke=1, fill=0)
    p.rect(margin_left + col_cod_descritor + col_descritor, y_position - line_height, col_eixo, line_height, stroke=1, fill=0)

    p.drawString(margin_left + 0.2 * cm, y_position - line_height + 0.2 * cm, "Código do Descritor")
    p.drawString(margin_left + col_cod_descritor + 0.2 * cm, y_position - line_height + 0.2 * cm, "Descritor")
    p.drawString(margin_left + col_cod_descritor + col_descritor + 0.2 * cm, y_position - line_height + 0.2 * cm, "Eixo")

    y_position -= line_height

    # Adicionar descritores com bordas dinâmicas
    p.setFont("Helvetica", 10)
    for descritor in descritores:
        if y_position < 2 * cm:  # Adicionar nova página se necessário
            p.showPage()
            p.setFont("Helvetica", 10)
            y_position = margin_top

        # Função para calcular linhas com quebra de texto
        def wrap_text(text, max_width):
            words = text.split()
            lines = []
            line = ""
            for word in words:
                if p.stringWidth(line + " " + word, "Helvetica", 10) < max_width:
                    line += " " + word
                else:
                    lines.append(line.strip())
                    line = word
            lines.append(line.strip())
            return lines

        # Quebras de linha em cada coluna
        cod_descritor_lines = wrap_text(descritor.cod_descritor, col_cod_descritor - 0.5 * cm)
        descritor_lines = wrap_text(descritor.descritor, col_descritor - 0.5 * cm)
        eixo_lines = wrap_text(descritor.eixo, col_eixo - 0.5 * cm)

        # Determinar altura dinâmica da célula
        max_lines = max(len(cod_descritor_lines), len(descritor_lines), len(eixo_lines))
        cell_height = max_lines * line_height

        # Bordas dinâmicas
        p.rect(margin_left, y_position - cell_height, col_cod_descritor, cell_height, stroke=1, fill=0)
        p.rect(margin_left + col_cod_descritor, y_position - cell_height, col_descritor, cell_height, stroke=1, fill=0)
        p.rect(margin_left + col_cod_descritor + col_descritor, y_position - cell_height, col_eixo, cell_height, stroke=1, fill=0)

        # Preencher as células com texto
        def draw_text_in_cell(x, y, lines):
            for i, line in enumerate(lines):
                p.drawString(x + 0.2 * cm, y - (i + 1) * line_height + 0.2 * cm, line)

        draw_text_in_cell(margin_left, y_position, cod_descritor_lines)
        draw_text_in_cell(margin_left + col_cod_descritor, y_position, descritor_lines)
        draw_text_in_cell(margin_left + col_cod_descritor + col_descritor, y_position, eixo_lines)

        # Ajustar posição vertical para a próxima linha
        y_position -= cell_height

    # Finalizar o PDF
    p.save()
    return response
