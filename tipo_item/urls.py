from django.urls import path
from .views import listar_tipos_item, cadastrar_tipo_item, editar_tipo_item, excluir_tipo_item

urlpatterns = [
    path('', listar_tipos_item, name='listar_tipos_item'),
    path('cadastrar/', cadastrar_tipo_item, name='cadastrar_tipo_item'),
    path('editar/<str:pk>/', editar_tipo_item, name='editar_tipo_item'),
    path('excluir/<str:pk>/', excluir_tipo_item, name='excluir_tipo_item'),
]
