# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from painel_bugs.models import FalhasEmAberto, FalhasEncerradasNosUltimos6Meses
from django.db.models import Sum, Count

@login_required(login_url='/login')
def ShowBugs(request):
    from datetime import datetime
    data = datetime.now()	
    FALHAS_ENCERRADAS_NOS_ULTIMOS_6_MESES = FalhasEncerradasNosUltimos6Meses.objects.raw("select 1 as id, count(*) as QUANTIDADE, DATE_FORMAT(data_criacao, '%%Y-%%m') AS ANO_MES from painel_falhas_encerredas_nos_ultimos_6_meses_logstash group by ANO_MES")
    FALHAS_EM_ABERTO = FalhasEmAberto.objects.all().values('tipo_servico').annotate(total=Count('tipo_servico')).order_by('-total')
    TOTAL_FALHAS_EM_ABERTO = FalhasEmAberto.objects.count()
    TOTAL_FALHAS_NOS_ULTIMOS_6_MESES = FalhasEncerradasNosUltimos6Meses.objects.count()
    return render(request, 'painel_bugs/bugs.html',
        {
            'data': data,		
            'FALHAS_EM_ABERTO': FALHAS_EM_ABERTO,
            'FALHAS_ENCERRADAS_NOS_ULTIMOS_6_MESES': FALHAS_ENCERRADAS_NOS_ULTIMOS_6_MESES,			
            'TOTAL_FALHAS_EM_ABERTO': TOTAL_FALHAS_EM_ABERTO,
            'TOTAL_FALHAS_NOS_ULTIMOS_6_MESES': TOTAL_FALHAS_NOS_ULTIMOS_6_MESES,
        })
def ShowBugs_tv(request):
    from datetime import datetime
    data = datetime.now()	
    FALHAS_ENCERRADAS_NOS_ULTIMOS_6_MESES = FalhasEncerradasNosUltimos6Meses.objects.raw("select 1 as id, count(*) as QUANTIDADE, DATE_FORMAT(data_criacao, '%%Y-%%m') AS ANO_MES from painel_falhas_encerredas_nos_ultimos_6_meses_logstash group by ANO_MES")
    FALHAS_EM_ABERTO = FalhasEmAberto.objects.all().values('tipo_servico').annotate(total=Count('tipo_servico')).order_by('-total')
    TOTAL_FALHAS_EM_ABERTO = FalhasEmAberto.objects.count()
    TOTAL_FALHAS_NOS_ULTIMOS_6_MESES = FalhasEncerradasNosUltimos6Meses.objects.count()
    return render(request, 'painel_bugs/bugs_tv.html',
        {
            'data': data,		
            'FALHAS_EM_ABERTO': FALHAS_EM_ABERTO,
            'FALHAS_ENCERRADAS_NOS_ULTIMOS_6_MESES': FALHAS_ENCERRADAS_NOS_ULTIMOS_6_MESES,			
            'TOTAL_FALHAS_EM_ABERTO': TOTAL_FALHAS_EM_ABERTO,
            'TOTAL_FALHAS_NOS_ULTIMOS_6_MESES': TOTAL_FALHAS_NOS_ULTIMOS_6_MESES,
        })
		


def GetDetalhamento (request):
	vServico = request.GET['tipo_servico']	
	detalhe_falhas = FalhasEmAberto.objects.filter(tipo_servico__contains = vServico).values().distinct().order_by('tipo_servico')	
	return render(request, 'painel_bugs/falhas_detalhamento.html',
        {  
            'detalhe_falhas': detalhe_falhas,				
        })			