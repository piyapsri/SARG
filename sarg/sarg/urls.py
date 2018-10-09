"""sarg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('django.contrib.auth.urls')),
    path('painel_bugs/', include('painel_bugs.urls')),
    path('painel_demandas/', include('painel_demandas.urls')),
    path('painel_incidentes/', include('painel_incidentes.urls')),
    path('painel_monitoracoes/', include('painel_monitoracoes.urls')),
    path('painel_gmuds/', include('painel_gmuds.urls')),
    path('painel_orcamentos/', include('painel_orcamentos.urls')),
    path('painel_oportunidades/', include('painel_oportunidades.urls')),
    path('painel_projetos/', include('painel_projetos.urls')),
    path('painel_ongoing/', include('painel_ongoing.urls')),
    path('painel_horas_gns/', include('painel_horas_gns.urls')),
    path('painel_rateio_horas/', include('painel_rateio_horas.urls')),
    path('receitas_extras_ongoing/', include('receitas_extras_ongoing.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
