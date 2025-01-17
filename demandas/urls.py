from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_demandas, name='listar_demandas'),
    path('cadastrar/', views.cadastrar_demanda, name='cadastrar_demanda'),
    path('<str:cod_demanda>/editar/', views.editar_demanda, name='editar_demanda'),  # Adicionado
    path('<str:cod_demanda>/gerar-itens/', views.gerar_itens, name='gerar_itens'),
    path('<str:cod_demanda>/', views.detalhar_demanda, name='detalhar_demanda'),
    path('<str:cod_demanda>/editar-itens/', views.editar_itens, name='editar_itens'),
]
