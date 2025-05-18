"""
URL configuration for plataforma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from usuarios.views import login_view, home_view
from django.conf import settings
from django.conf.urls.static import static
from subprogramas import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', login_view, name='home'),
    path('home/', home_view, name='home'),
    path('', include('usuarios.urls')),
    path('grupos/', include('grupos.urls')),
    path('usuario_grupo/', include('usuario_grupo.urls')),
    path('anos/', include('anos.urls')),
    path('disciplinas/', include('disciplinas.urls')),
    path('ensinos/', include('ensinos.urls')),
    path('etapas/', include('etapas.urls')),
    path('descritores/', include('descritores.urls')),
    path('tipo_item/', include('tipo_item.urls')),
    path('padrao_item/', include('padrao_item.urls')),
    path('programas/', include('programas.urls')),
    path('subprogramas/', include('subprogramas.urls')),
    path('matrizes/', include('matrizes.urls')),
    path('demandas/', include('demandas.urls')),
    path('elaborar_itens/', include('elaborar_itens.urls')),
    path('ajax/load-subprogramas/', views.load_subprogramas, name='ajax_load_subprogramas'),
    path('revisao/', include('revisao.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

