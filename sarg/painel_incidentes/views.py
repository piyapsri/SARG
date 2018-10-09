# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from painel_incidentes.models import OcorrenciasEmAberto, OcorrenciasEmAbertoGraph, OcorrenciasAbertasNoMes, OcorrenciasEncerradasMesAtual

from django.db.models import Sum, Count

@login_required(login_url='/login')
def ShowIncidentes(request):
    from datetime import datetime
    data = datetime.now()	
    OCORRENCIAS_EM_ABERTO = OcorrenciasEmAbertoGraph.objects.all()   
    OCORRENCIAS_ENCERRADAS_MES_ATUAL = OcorrenciasEncerradasMesAtual.objects.values('tipo_servico').exclude(tipo_servico='GSR - INTERNO').annotate(total=Count('tipo_servico')).order_by('-total')
    TOTAL_OCORRENCIAS_EM_ABERTO = OcorrenciasEmAberto.objects.exclude(tipo_servico='GSR - INTERNO').count()
    TOTAL_OCORRENCIAS_ABERTAS_NO_MES = OcorrenciasAbertasNoMes.objects.exclude(tipo_servico='GSR - INTERNO').count()
    TOTAL_OCORRENCIAS_ENCERRADAS_MES_ATUAL = OcorrenciasEncerradasMesAtual.objects.exclude(tipo_servico='GSR - INTERNO').count()
    return render(request, 'painel_incidentes/incidentes.html',
        {
            'data': data,
            'OCORRENCIAS_EM_ABERTO': OCORRENCIAS_EM_ABERTO,
            'OCORRENCIAS_ENCERRADAS_MES_ATUAL': OCORRENCIAS_ENCERRADAS_MES_ATUAL, 
            'TOTAL_OCORRENCIAS_EM_ABERTO': TOTAL_OCORRENCIAS_EM_ABERTO, 
            'TOTAL_OCORRENCIAS_ABERTAS_NO_MES': TOTAL_OCORRENCIAS_ABERTAS_NO_MES,
            'TOTAL_OCORRENCIAS_ENCERRADAS_MES_ATUAL': TOTAL_OCORRENCIAS_ENCERRADAS_MES_ATUAL, 			
        })
		
def GetDetalhamento (request):
	vSituacao = request.GET['situacao']
	if vSituacao == 'AGUARDANDO':
		vSituacao = 'Aguardando o solicitante'
	elif vSituacao == 'ATENDIMENTO':
		vSituacao = 'Em atendimento'
	elif vSituacao == 'ENCAMINHADO':
		vSituacao = 'Encaminhada'
	else:
		vSituacao = 'None'
	vServico = request.GET['tipo_servico']	
	detalhe_ocorrencias = OcorrenciasEmAberto.objects.filter(situacao = vSituacao, tipo_servico__contains = vServico).values().distinct().order_by('tipo_servico')	
	return render(request, 'painel_incidentes/ocorrencias_detalhamento.html',
        {  
            'detalhe_ocorrencias': detalhe_ocorrencias,				
        })	
		
def ShowIncidentes_tv(request):
    from datetime import datetime
    data = datetime.now()
    OCORRENCIAS_EM_ABERTO = OcorrenciasEmAbertoGraph.objects.all()
    OCORRENCIAS_ENCERRADAS_MES_ATUAL = OcorrenciasEncerradasMesAtual.objects.values('tipo_servico').exclude(tipo_servico='GSR - INTERNO').annotate(total=Count('tipo_servico')).order_by('-total')
    TOTAL_OCORRENCIAS_EM_ABERTO = OcorrenciasEmAberto.objects.exclude(tipo_servico='GSR - INTERNO').count()
    TOTAL_OCORRENCIAS_ABERTAS_NO_MES = OcorrenciasAbertasNoMes.objects.exclude(tipo_servico='GSR - INTERNO').count()
    TOTAL_OCORRENCIAS_ENCERRADAS_MES_ATUAL = OcorrenciasEncerradasMesAtual.objects.exclude(tipo_servico='GSR - INTERNO').count()

    return render(request, 'painel_incidentes/incidentes_tv.html',
        {
            'data': data,
            'OCORRENCIAS_EM_ABERTO': OCORRENCIAS_EM_ABERTO,
            'OCORRENCIAS_ENCERRADAS_MES_ATUAL': OCORRENCIAS_ENCERRADAS_MES_ATUAL, 
            'TOTAL_OCORRENCIAS_EM_ABERTO': TOTAL_OCORRENCIAS_EM_ABERTO, 
            'TOTAL_OCORRENCIAS_ABERTAS_NO_MES': TOTAL_OCORRENCIAS_ABERTAS_NO_MES,
            'TOTAL_OCORRENCIAS_ENCERRADAS_MES_ATUAL': TOTAL_OCORRENCIAS_ENCERRADAS_MES_ATUAL, 		
        })

