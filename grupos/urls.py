from django.urls import path
from .views import cadastrar_grupo, editar_grupo, excluir_grupo

urlpatterns = [
    path('cadastrar_grupo/', cadastrar_grupo, name='cadastrar_grupo'),
    path('editar_grupo/<str:pk>/', editar_grupo, name='editar_grupo'),
    path('excluir_grupo/<str:pk>/', excluir_grupo, name='excluir_grupo'),
]
