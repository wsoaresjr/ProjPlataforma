from django.urls import path
from .views import listar_etapas, cadastrar_etapa, editar_etapa, excluir_etapa

urlpatterns = [
    path('', listar_etapas, name='listar_etapas'),
    path('cadastrar/', cadastrar_etapa, name='cadastrar_etapa'),
    path('editar/<str:pk>/', editar_etapa, name='editar_etapa'),
    path('excluir/<str:pk>/', excluir_etapa, name='excluir_etapa'),
]
