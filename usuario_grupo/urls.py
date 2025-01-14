from django.urls import path
from .views import associar_usuario_grupo, editar_associacao, excluir_associacao

urlpatterns = [
    path('associar/', associar_usuario_grupo, name='associar_usuario_grupo'),
    path('editar/<int:pk>/', editar_associacao, name='editar_associacao'),
    path('excluir/<int:pk>/', excluir_associacao, name='excluir_associacao'),
]
