from django.urls import path
from .views import listar_disciplinas, cadastrar_disciplina, editar_disciplina, excluir_disciplina

urlpatterns = [
    path('', listar_disciplinas, name='listar_disciplinas'),
    path('cadastrar/', cadastrar_disciplina, name='cadastrar_disciplina'),
    path('editar/<str:pk>/', editar_disciplina, name='editar_disciplina'),
    path('excluir/<str:pk>/', excluir_disciplina, name='excluir_disciplina'),
]
