from django.urls import path

from . import views

urlpatterns = [
    path('bugs', views.ShowBugs),
    path('bugs_tv', views.ShowBugs_tv),
	path('falhas_detalhamento.html',  views.GetDetalhamento),
]
