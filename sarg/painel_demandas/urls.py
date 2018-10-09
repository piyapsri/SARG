from django.urls import path

from . import views

urlpatterns = [
    path('demandas', views.ShowDemandas),
    path('demandas_tv', views.ShowDemandas_tv),
    path('demandas_naoorcadas.html',  views.GetDetalhamentoNaoOrcadas),
    path('demandas_detalhamento.html',  views.GetDetalhamento),
]
