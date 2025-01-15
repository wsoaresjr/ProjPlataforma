from django.urls import path
from .views import listar_subprogramas, cadastrar_subprograma, editar_subprograma, excluir_subprograma

urlpatterns = [
    path('', listar_subprogramas, name='listar_subprogramas'),
    path('cadastrar/', cadastrar_subprograma, name='cadastrar_subprograma'),
    path('editar/<str:pk>/', editar_subprograma, name='editar_subprograma'),
    path('excluir/<str:pk>/', excluir_subprograma, name='excluir_subprograma'),
]
