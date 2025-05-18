from django.urls import path
from .views import painel_revisao, revisar_item

urlpatterns = [
    # GET  /revisao/painel/           → lista itens para revisar
    path('painel/', painel_revisao, name='painel_revisao'),

    # GET/POST  /revisao/revisar/<cod_item>/  → revisa um item
    path('revisar/<str:cod_item>/', revisar_item, name='revisar_item'),
]
