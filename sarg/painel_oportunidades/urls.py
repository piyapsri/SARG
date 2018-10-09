from django.urls import path

from . import views

urlpatterns = [
    path('oportunidades', views.ShowOportunities),
    path('oportunidades_tv', views.ShowOportunities_tv),
    path('oportunidades2_tv', views.ShowOportunities2_tv),
    path('oportunidades3_tv', views.ShowOportunities3_tv),
]

