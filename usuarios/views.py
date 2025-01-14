from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from usuarios.models import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Busca o usuário pelo username
            user = Usuario.objects.get(username=username)

            # Verifica se a senha informada corresponde à senha criptografada
            if check_password(password, user.senha):
                # Salva informações do usuário na sessão
                request.session['usuario_id'] = user.cod_usuario
                request.session['usuario_nome'] = user.nome

                # Redireciona para a página inicial após login bem-sucedido
                return redirect('home')
            else:
                return render(request, 'usuarios/login.html', {'error': 'Usuário ou senha inválidos'})

        except Usuario.DoesNotExist:
            # Retorna mensagem de erro se o usuário não for encontrado
            return render(request, 'usuarios/login.html', {'error': 'Usuário ou senha inválidos'})

    # Exibe a página de login caso seja um GET
    return render(request, 'usuarios/login.html')






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

