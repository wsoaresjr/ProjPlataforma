from django.shortcuts import render, redirect
from .models import Usuario
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            senha = form.cleaned_data['senha']
            try:
                usuario = Usuario.objects.get(username=username)
                if usuario.check_password(senha) and usuario.status_ativo:
                    # Salvar informações do usuário na sessão
                    request.session['usuario_id'] = usuario.cod_usuario
                    request.session['usuario_nome'] = usuario.nome
                    return redirect('home')  # Altere para sua rota de sucesso
                else:
                    form.add_error(None, "Credenciais inválidas ou usuário inativo.")
            except Usuario.DoesNotExist:
                form.add_error(None, "Usuário não encontrado.")
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


from django.shortcuts import render, redirect
from usuarios.models import Usuario
from grupos.models import Grupo
from usuario_grupo.models import UsuarioGrupo

def home_view(request):
    # Verificar se o usuário está autenticado
    if 'usuario_id' not in request.session:
        return redirect('/')  # Redirecionar para a página de login

    # Buscar o usuário e os grupos aos quais ele pertence
    usuario_id = request.session['usuario_id']
    usuario_nome = request.session['usuario_nome']
    grupos = UsuarioGrupo.objects.filter(usuario__cod_usuario=usuario_id).values_list('grupo__nome_grupo', flat=True)

    # Verificar se o usuário é administrador
    is_admin = 'Administradores' in grupos

    # Obter lista de usuários, grupos e associações se o usuário for administrador
    usuarios = Usuario.objects.all() if is_admin else None
    grupos_lista = Grupo.objects.all() if is_admin else None
    associacoes = UsuarioGrupo.objects.all() if is_admin else None

    return render(request, 'usuarios/home.html', {
        'usuario_nome': usuario_nome,
        'grupos': grupos,
        'is_admin': is_admin,
        'usuarios': usuarios,
        'grupos_lista': grupos_lista,
        'associacoes': associacoes,
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

