from django.urls import path
from .views import listar_programas, cadastrar_programa, editar_programa, excluir_programa

urlpatterns = [
    path('', listar_programas, name='listar_programas'),
    path('cadastrar/', cadastrar_programa, name='cadastrar_programa'),
    path('editar/<str:pk>/', editar_programa, name='editar_programa'),
    path('excluir/<str:pk>/', excluir_programa, name='excluir_programa'),
]
