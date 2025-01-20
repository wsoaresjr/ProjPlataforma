from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_itens, name='listar_itens'),
    path('<str:cod_item>/', views.elaborar_item, name='elaborar_item'),
]
