from django.urls import path

from . import views

urlpatterns = [
    path('gmuds', views.ShowGmuds),
    path('gmuds_tv', views.ShowGmuds_tv),
]
