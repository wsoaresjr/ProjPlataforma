from django.urls import path
from .views import listar_ensinos, cadastrar_ensino, editar_ensino, excluir_ensino

urlpatterns = [
    path('', listar_ensinos, name='listar_ensinos'),
    path('cadastrar/', cadastrar_ensino, name='cadastrar_ensino'),
    path('editar/<str:pk>/', editar_ensino, name='editar_ensino'),
    path('excluir/<str:pk>/', excluir_ensino, name='excluir_ensino'),
]
