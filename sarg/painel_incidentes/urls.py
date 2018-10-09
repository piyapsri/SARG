from django.urls import path

from . import views

urlpatterns = [
    path('incidentes', views.ShowIncidentes),
    path('incidentes_tv', views.ShowIncidentes_tv),
    path('ocorrencias_detalhamento.html',  views.GetDetalhamento),	
]
