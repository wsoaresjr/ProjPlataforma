from django.urls import path
from . import views 
from .views import listar_matrizes, cadastrar_matriz, editar_matriz, excluir_matriz, visualizar_matriz

urlpatterns = [
    path('', listar_matrizes, name='listar_matrizes'),
    path('cadastrar/', cadastrar_matriz, name='cadastrar_matriz'),
    path('editar/<str:pk>/', editar_matriz, name='editar_matriz'),
    path('excluir/<str:pk>/', excluir_matriz, name='excluir_matriz'),
    path('visualizar/<str:pk>/', visualizar_matriz, name='visualizar_matriz'),
    path('filtrar_subprogramas/', views.filtrar_subprogramas, name='filtrar_subprogramas'),
    path('filtrar_descritores/', views.filtrar_descritores, name='filtrar_descritores'),
    path('ver/<str:cod_matriz>/', views.ver_matriz, name='ver_matriz'),
    path('exportar_excel/<str:cod_matriz>/', views.exportar_matriz_excel, name='exportar_matriz_excel'),
    path('exportar_pdf/<str:cod_matriz>/', views.exportar_matriz_pdf, name='exportar_matriz_pdf'),
]
