from django.urls import path

from . import views

urlpatterns = [
    path('monitoracoes', views.ShowMonitoracoes),
    path('painel_monitoracoes_teste', views.ShowMonitoracoesTeste),
]
