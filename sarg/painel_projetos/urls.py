from django.urls import path

from . import views

urlpatterns = [
    path('projetos', views.ShowProjects),
    path('projetos_tv', views.ShowProjects_tv),
    path('projetos2_tv', views.ShowProjects2_tv),
    path('projetos3_tv', views.ShowProjects3_tv),
]

