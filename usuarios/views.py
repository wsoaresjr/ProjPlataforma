from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from usuarios.models import Usuario
from usuario_grupo.models import UsuarioGrupo

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Usuario.objects.get(username=username)
            if check_password(password, user.senha):
                request.session['usuario_id'] = user.cod_usuario
                request.session['usuario_nome'] = user.nome

                # Busca todos os grupos do usuário
                grupos_usuario = UsuarioGrupo.objects.filter(usuario=user).values_list('grupo__nome_grupo', flat=True)

                if 'Revisores' in grupos_usuario:
                    return redirect('painel_revisao')  # Redireciona para a home do revisor
                elif 'Elaboradores' in grupos_usuario:
                    return redirect('listar_itens')
                else:
                    return redirect('home')
            else:
                return render(request, 'usuarios/login.html', {'error': 'Usuário ou senha inválidos'})
        except Usuario.DoesNotExist:
            return render(request, 'usuarios/login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'usuarios/login.html')






from django.shortcuts import render, redirect
from usuarios.models import Usuario
from grupos.models import Grupo
from usuario_grupo.models import UsuarioGrupo
from anos.models import Ano
from disciplinas.models import Disciplina
from ensinos.models import Ensino
from etapas.models import Etapa
from descritores.models import Descritor
from tipo_item.models import TipoItem
from padrao_item.models import PadraoItem
from programas.models import Programa
from subprogramas.models import Subprograma
from matrizes.models import Matriz
from demandas.models import Demanda
from demandas.models import Item

def home_view(request):
    # Verificar se o usuário está autenticado
    if 'usuario_id' not in request.session:
        return redirect('/')  # Redirecionar para a página de login

    # Buscar o usuário e seus grupos
    usuario_id = request.session['usuario_id']
    usuario_nome = request.session['usuario_nome']
    grupos = UsuarioGrupo.objects.filter(usuario__cod_usuario=usuario_id).values_list('grupo__nome_grupo', flat=True)

    # Verificar o grupo do usuário
    is_admin = 'Administradores' in grupos
    is_modelagem = 'Modelagem' in grupos
    is_elaborador = 'Elaboradores' in grupos

    # Dados para administradores
    usuarios = Usuario.objects.all() if is_admin else None
    grupos_lista = Grupo.objects.all() if is_admin else None
    associacoes = UsuarioGrupo.objects.all() if is_admin else None
    anos = Ano.objects.all() if is_admin else None
    disciplinas = Disciplina.objects.all() if is_admin else None
    ensinos = Ensino.objects.all() if is_admin else None
    etapas = Etapa.objects.all() if is_admin else None
    descritores = Descritor.objects.all() if is_admin else None
    tipos_item = TipoItem.objects.all() if is_admin else None
    padroes_item = PadraoItem.objects.all() if is_admin else None
    programas_admin = Programa.objects.all() if is_admin else None
    subprogramas_admin = Subprograma.objects.all() if is_admin else None
    matrizes_admin = Matriz.objects.all() if is_admin else None

    # Dados para modelagem
    programas_modelagem = Programa.objects.all() if is_modelagem else None
    subprogramas_modelagem = Subprograma.objects.all() if is_modelagem else None
    matrizes_modelagem = Matriz.objects.filter(programa__in=programas_modelagem) if is_modelagem else None
    demandas = Demanda.objects.all() if is_modelagem else None

    # Dados para Elaboradores
    itens_para_elaborar = Item.objects.filter(elaborador__cod_usuario=usuario_id, status_item="A Elaborar") if is_elaborador else None

    return render(request, 'usuarios/home.html', {
        'usuario_nome': usuario_nome,
        'grupos': grupos,
        'is_admin': is_admin,
        'is_modelagem': is_modelagem,
        'usuarios': usuarios,
        'grupos_lista': grupos_lista,
        'associacoes': associacoes,
        'anos': anos,
        'disciplinas': disciplinas,
        'ensinos': ensinos,
        'etapas': etapas,
        'descritores': descritores,
        'tipos_item': tipos_item,
        'padroes_item': padroes_item,
        'programas': programas_admin if is_admin else programas_modelagem,
        'subprogramas': subprogramas_admin if is_admin else subprogramas_modelagem,
        'matrizes': matrizes_admin if is_admin else matrizes_modelagem,
        'demandas': demandas,
        'is_elaborador': is_elaborador,
        'itens_para_elaborar': itens_para_elaborar,
    })






from django.http import HttpResponseNotAllowed

def logout_view(request):
    if request.method == 'POST':
        # Limpar a sessão para deslogar o usuário
        request.session.flush()
        return redirect('/')  # Redirecionar para a página de login
    return HttpResponseNotAllowed(['POST'])



from django.shortcuts import render, redirect
from .forms import UsuarioForm

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])  # Aplicar hash à senha
            usuario.save()
            return redirect('home')  # Redirecionar para a página inicial
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})



from django.shortcuts import get_object_or_404

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            if 'senha' in form.cleaned_data and form.cleaned_data['senha']:
                usuario.set_password(form.cleaned_data['senha'])  # Aplicar hash à senha
            usuario.save()
            return redirect('home')  # Redirecionar para a página inicial
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario': usuario})


from django.shortcuts import get_object_or_404

def excluir_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('home')  # Redirecionar para a página inicial após exclusão
    return render(request, 'usuarios/excluir_usuario.html', {'usuario': usuario})

