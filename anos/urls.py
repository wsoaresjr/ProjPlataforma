from django.urls import path
from .views import listar_anos, cadastrar_ano, editar_ano, excluir_ano

urlpatterns = [
    path('', listar_anos, name='listar_anos'),  # Adicionar a rota para listar anos
    path('cadastrar/', cadastrar_ano, name='cadastrar_ano'),
    path('editar/<str:pk>/', editar_ano, name='editar_ano'),
    path('excluir/<str:pk>/', excluir_ano, name='excluir_ano'),
]
