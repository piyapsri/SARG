from django.urls import path

from . import views

urlpatterns = [
    path('ongoing', views.ShowOngoing),
]
