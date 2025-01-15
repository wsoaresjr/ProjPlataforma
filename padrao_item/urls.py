from django.urls import path
from .views import listar_padroes_item, cadastrar_padrao_item, editar_padrao_item, excluir_padrao_item

urlpatterns = [
    path('', listar_padroes_item, name='listar_padroes_item'),
    path('cadastrar/', cadastrar_padrao_item, name='cadastrar_padrao_item'),
    path('editar/<str:pk>/', editar_padrao_item, name='editar_padrao_item'),
    path('excluir/<str:pk>/', excluir_padrao_item, name='excluir_padrao_item'),
]
