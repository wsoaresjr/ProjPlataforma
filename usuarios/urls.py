from django.urls import path
from .views import login_view, home_view, logout_view, cadastrar_usuario, editar_usuario, excluir_usuario

urlpatterns = [
    path('', login_view, name='home'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('editar_usuario/<str:pk>/', editar_usuario, name='editar_usuario'),  # Alterado de <int:pk> para <str:pk>
    path('excluir_usuario/<str:pk>/', excluir_usuario, name='excluir_usuario'),
]
