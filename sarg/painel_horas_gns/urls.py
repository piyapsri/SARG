from django.urls import path

from . import views

urlpatterns = [
    path('horasgns', views.getResumoHoras),
    path('horasgns_detalhe', views.getDetalhamentoHrs),
]
