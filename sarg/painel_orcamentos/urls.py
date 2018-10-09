from django.urls import path

from . import views
app_name = 'painel_orcamentos'


urlpatterns = [
    path('orcamentos', views.ShowOrcamentos),
    path('orcamentos_detailed', views.ShowOrcamentosDetailed),
    path('orcamentos_detailed/orcamentos_detailed_ic/<ic>/', views.ShowOrcamentosDetailedIC),
    path('orcamentos_detailed/orcamentos_detailed_ic_ano/<ic>/', views.ShowOrcamentosDetailedICAno),	
]
