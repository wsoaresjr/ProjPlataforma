from django.urls import path
from .views import listar_descritores, cadastrar_descritor, editar_descritor, excluir_descritor
from descritores import views as descritores_views

urlpatterns = [
    path('', listar_descritores, name='listar_descritores'),
    path('cadastrar/', cadastrar_descritor, name='cadastrar_descritor'),
    path('editar/<str:pk>/', editar_descritor, name='editar_descritor'),
    path('excluir/<str:pk>/', excluir_descritor, name='excluir_descritor'),
    path('ajax/load-descritores/', descritores_views.load_descritores, name='ajax_load_descritores'),
]
