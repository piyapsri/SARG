# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from painel_demandas.models import DEMANDAS
from django.db.models import Sum

@login_required(login_url='/login')
def ShowDemandas(request):
    from datetime import datetime
    data = datetime.now()
    DEMANDAS_SERVICOS=DEMANDAS.objects.raw('''
	    SELECT
		1 as id,
        `sarg`.`painel_demandas_logstash`.`servico` AS `servico`,
        SUM((CASE
            WHEN (`sarg`.`painel_demandas_logstash`.`tipo` = 'EXTERNAS') THEN 1
            ELSE 0
        END)) AS `EXTERNAS`,
        SUM((CASE
            WHEN (`sarg`.`painel_demandas_logstash`.`tipo` = 'INTERNAS') THEN 1
            ELSE 0
        END)) AS `INTERNAS`,
        COUNT(0) AS `TOTAL`,
        SUM((CASE
            WHEN
                ((`sarg`.`painel_demandas_logstash`.`tipo` = 'EXTERNAS')
                    AND (`sarg`.`painel_demandas_logstash`.`servico` = `sarg`.`painel_demandas_logstash`.`servico`))
            THEN
                `sarg`.`painel_demandas_logstash`.`horas_previstas`
            ELSE 0
        END)) AS `HORAS_EXTERNAS`,
        IFNULL(SUM((CASE
                    WHEN
                        ((`sarg`.`painel_demandas_logstash`.`tipo` = 'INTERNAS')
                            AND (`sarg`.`painel_demandas_logstash`.`servico` = `sarg`.`painel_demandas_logstash`.`servico`))
                    THEN
                        `sarg`.`painel_demandas_logstash`.`horas_previstas`
                    ELSE 0
                END)),
                0) AS `HORAS_INTERNAS`,
        IFNULL(SUM(`sarg`.`painel_demandas_logstash`.`horas_previstas`),
                0) AS `HORAS_TOTAL`
    FROM
        `sarg`.`painel_demandas_logstash`
    GROUP BY `sarg`.`painel_demandas_logstash`.`servico`
    ORDER BY `TOTAL` DESC , `sarg`.`painel_demandas_logstash`.`servico`
	''')
    QUANTIDADE_DEMANDAS_EXTERNAS_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=False, severidade = 'Demanda').count()
    QUANTIDADE_DEMANDAS_EXTERNAS_NAO_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=True, severidade = 'Demanda').count()
    TOTAL_DEMANDAS_EXTERNAS = DEMANDAS.objects.filter(severidade = 'Demanda').count()
	
    QUANTIDADE_DEMANDAS_INTERNAS_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=False, severidade = 'Severidade 9').count()
    QUANTIDADE_DEMANDAS_INTERNAS_NAO_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=True, severidade = 'Severidade 9').count()
    TOTAL_DEMANDAS_INTERNAS = DEMANDAS.objects.filter(severidade = 'Severidade 9').count()
	
    TOTAL_DEMANDAS_EXTERNAS_E_INTERNAS = DEMANDAS.objects.count()
	

    return render(request, 'painel_demandas/demandas.html',
        {
            'data': data,
            'DEMANDAS_SERVICOS': DEMANDAS_SERVICOS,		
            'QUANTIDADE_DEMANDAS_EXTERNAS_ORCADAS': QUANTIDADE_DEMANDAS_EXTERNAS_ORCADAS,
            'QUANTIDADE_DEMANDAS_EXTERNAS_NAO_ORCADAS': QUANTIDADE_DEMANDAS_EXTERNAS_NAO_ORCADAS,
            'QUANTIDADE_DEMANDAS_INTERNAS_ORCADAS': QUANTIDADE_DEMANDAS_INTERNAS_ORCADAS,
            'QUANTIDADE_DEMANDAS_INTERNAS_NAO_ORCADAS': QUANTIDADE_DEMANDAS_INTERNAS_NAO_ORCADAS,
            'TOTAL_DEMANDAS_EXTERNAS': TOTAL_DEMANDAS_EXTERNAS,
            'TOTAL_DEMANDAS_INTERNAS': TOTAL_DEMANDAS_INTERNAS,
            'TOTAL_DEMANDAS_EXTERNAS_E_INTERNAS': TOTAL_DEMANDAS_EXTERNAS_E_INTERNAS,

        })
def ShowDemandas_tv(request):
    from datetime import datetime
    data = datetime.now()
    DEMANDAS_SERVICOS=DEMANDAS.objects.raw('''
	    SELECT
		1 as id,
        `sarg`.`painel_demandas_logstash`.`servico` AS `servico`,
        SUM((CASE
            WHEN (`sarg`.`painel_demandas_logstash`.`tipo` = 'EXTERNAS') THEN 1
            ELSE 0
        END)) AS `EXTERNAS`,
        SUM((CASE
            WHEN (`sarg`.`painel_demandas_logstash`.`tipo` = 'INTERNAS') THEN 1
            ELSE 0
        END)) AS `INTERNAS`,
        COUNT(0) AS `TOTAL`,
        SUM((CASE
            WHEN
                ((`sarg`.`painel_demandas_logstash`.`tipo` = 'EXTERNAS')
                    AND (`sarg`.`painel_demandas_logstash`.`servico` = `sarg`.`painel_demandas_logstash`.`servico`))
            THEN
                `sarg`.`painel_demandas_logstash`.`horas_previstas`
            ELSE 0
        END)) AS `HORAS_EXTERNAS`,
        IFNULL(SUM((CASE
                    WHEN
                        ((`sarg`.`painel_demandas_logstash`.`tipo` = 'INTERNAS')
                            AND (`sarg`.`painel_demandas_logstash`.`servico` = `sarg`.`painel_demandas_logstash`.`servico`))
                    THEN
                        `sarg`.`painel_demandas_logstash`.`horas_previstas`
                    ELSE 0
                END)),
                0) AS `HORAS_INTERNAS`,
        IFNULL(SUM(`sarg`.`painel_demandas_logstash`.`horas_previstas`),
                0) AS `HORAS_TOTAL`
    FROM
        `sarg`.`painel_demandas_logstash`
    GROUP BY `sarg`.`painel_demandas_logstash`.`servico`
    ORDER BY `TOTAL` DESC , `sarg`.`painel_demandas_logstash`.`servico`
	''')
    QUANTIDADE_DEMANDAS_EXTERNAS_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=False, severidade = 'Demanda').count()
    QUANTIDADE_DEMANDAS_EXTERNAS_NAO_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=True, severidade = 'Demanda').count()
    TOTAL_DEMANDAS_EXTERNAS = DEMANDAS.objects.filter(severidade = 'Demanda').count()
	
    QUANTIDADE_DEMANDAS_INTERNAS_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=False, severidade = 'Severidade 9').count()
    QUANTIDADE_DEMANDAS_INTERNAS_NAO_ORCADAS = DEMANDAS.objects.filter(horas_previstas__isnull=True, severidade = 'Severidade 9').count()
    TOTAL_DEMANDAS_INTERNAS = DEMANDAS.objects.filter(severidade = 'Severidade 9').count()
	
    TOTAL_DEMANDAS_EXTERNAS_E_INTERNAS = DEMANDAS.objects.count()
	

    return render(request, 'painel_demandas/demandas_tv.html',
        {
            'data': data,
            'DEMANDAS_SERVICOS': DEMANDAS_SERVICOS,		
            'QUANTIDADE_DEMANDAS_EXTERNAS_ORCADAS': QUANTIDADE_DEMANDAS_EXTERNAS_ORCADAS,
            'QUANTIDADE_DEMANDAS_EXTERNAS_NAO_ORCADAS': QUANTIDADE_DEMANDAS_EXTERNAS_NAO_ORCADAS,
            'QUANTIDADE_DEMANDAS_INTERNAS_ORCADAS': QUANTIDADE_DEMANDAS_INTERNAS_ORCADAS,
            'QUANTIDADE_DEMANDAS_INTERNAS_NAO_ORCADAS': QUANTIDADE_DEMANDAS_INTERNAS_NAO_ORCADAS,
            'TOTAL_DEMANDAS_EXTERNAS': TOTAL_DEMANDAS_EXTERNAS,
            'TOTAL_DEMANDAS_INTERNAS': TOTAL_DEMANDAS_INTERNAS,
            'TOTAL_DEMANDAS_EXTERNAS_E_INTERNAS': TOTAL_DEMANDAS_EXTERNAS_E_INTERNAS,

        })

		
def GetDetalhamento (request):
	vTipo = request.GET['tipo']
	vServico = request.GET['servico']	
	detalhe_demanda = DEMANDAS.objects.raw('''
SELECT
	1 as id,
    numero_ocorrencia,
    titulo,
    situacao,
    responsavel,
    horas_previstas
FROM
    sarg.vw_painel_demandas_logstash
WHERE
    tipo = '%s' AND servico like '%s'
	''' % (vTipo, vServico))
	return render(request, 'painel_demandas/demandas_detalhamento.html',
        {  
            'detalhe_demanda': detalhe_demanda,				
        })	

def GetDetalhamentoNaoOrcadas (request):
    vSeveridade = request.GET['severidade']
    DEMANDAS_NAOORCADAS = DEMANDAS.objects.raw('''
SELECT
	1 as id,
    numero_ocorrencia,
    titulo,
    situacao,
    responsavel,
    horas_previstas
FROM
    sarg.vw_painel_demandas_logstash
WHERE
    horas_previstas is null 
AND severidade like '%s'
	''' % vSeveridade) 
    return render(request, 'painel_demandas/demandas_naoorcadas.html',
        {  
            'DEMANDAS_NAOORCADAS': DEMANDAS_NAOORCADAS,	
        })
