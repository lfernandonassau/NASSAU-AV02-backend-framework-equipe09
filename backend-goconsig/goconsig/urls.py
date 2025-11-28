"""
URL configuration for gocosing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
# =============================================
# Importar ViewSets
from app_usuarios.views import ClienteViewSet
from app_parceiros.views import ParceiroViewSet
from app_emprestimos.views import SimulacaoViewSet
from app_historico.views import HistoricoSimulacaoListAPIView
from app_bancos.views import BancoViewSet
# =============================================
from rest_framework.routers import DefaultRouter 
from app_core import views as core_views
from app_usuarios import views as usuarios_views
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'parceiros', ParceiroViewSet)
router.register(r'bancos', BancoViewSet)
router.register(r'simulacoes', SimulacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #rota, views responsável, nome de referência
    path('api/', include(router.urls)),
    
    # Histórico de Simulações
    # endpoint por simulacao id
    path('simulacoes/<int:sim_id>/historico/', HistoricoSimulacaoListAPIView.as_view(), name='historico-por-simulacao'),
    # ou endpoint query:
    path('historico/', HistoricoSimulacaoListAPIView.as_view(), name='historico-list'),
    
    #React
    path('', TemplateView.as_view(template_name='index.html')),


    #GoCosing.com.br
    #path('', core_views.home, name='home'),
    
    #Login
    #path('login/', usuarios_views.login, name='login'),
    #Cadastro
    #path('cadastro/', usuarios_views.cadastro, name='cadastro'),           
]
