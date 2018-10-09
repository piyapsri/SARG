# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Max

# Create your views here.
from django.contrib.auth.decorators import login_required
from painel_horas_gns.models import ResumoRateioHorasGns
from clientes.models import Clientes
from django.db.models import Sum, Count, Value, Q

@login_required(login_url='/login')
def getResumoHoras(request):
    from datetime import datetime
    res = ResumoRateioHorasGns.objects.filter().aggregate(max_per=Max('periodo'))
    vPeriodo = request.POST.get('periodo', res.get('max_per'))
    vCliente = request.POST.get('cliente')
    vServico = request.POST.get('servico')
 #   vDescricao = request.POST.get("descricao")
	
    
    data = datetime.now()
    resumoHorasGns = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, descricao, sum(FN_FORMATA_HORA(round(qtd_horas), 'H')) qtd_horas FROM painel_rateio_horas_por_ic_ativ_logstash WHERE periodo = '%s' AND descricao !='Treinamento' AND descricao !='Melhoria' AND descricao !='Reunião' AND descricao !='Sem Categoria' AND descricao !='Demandas' AND descricao !='Chamados' group by id_tipo, descricao" % vPeriodo)
    ResumoHorasGns = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, descricao, sum(FN_FORMATA_HORA(round(qtd_horas), 'H')) qtd_horas FROM painel_rateio_horas_por_ic_ativ_logstash WHERE periodo = '%s' group by id_tipo, descricao" % vPeriodo)
	
    resumoHorasGnsProducao = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, descricao, sum(FN_FORMATA_HORA(round(qtd_horas), 'H')) qtd_horas FROM painel_rateio_horas_por_ic_ativ_logstash WHERE periodo = '%s' AND descricao !='Pré-venda' AND descricao !='Projetos' AND descricao !='Treinamento' AND descricao !='Melhoria' AND descricao !='Reunião' AND descricao !='Sem Categoria' group by id_tipo, descricao" % vPeriodo)
    resumoHorasGnsInterno = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, descricao, sum(FN_FORMATA_HORA(round(qtd_horas), 'H')) qtd_horas FROM painel_rateio_horas_por_ic_ativ_logstash WHERE periodo = '%s' AND descricao !='Pré-venda' AND descricao !='Projetos' AND descricao !='Demandas' AND descricao !='Chamados' group by id_tipo, descricao" % vPeriodo)
	#resumoHorasGns = ResumoRateioHorasGns.objects.all()
    totalHoras = ResumoRateioHorasGns.objects.filter(periodo = '%s' % (vPeriodo)).aggregate(Sum('qtd_horas'))['qtd_horas__sum']
    periodos = ResumoRateioHorasGns.objects.raw("SELECT p.periodo, max(p.id_tipo) id_tipo FROM painel_rateio_horas_por_ic_ativ_logstash p GROUP BY p.periodo ORDER BY p.periodo DESC")
    Periodos = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, periodo from painel_rateio_horas_por_ic_ativ_logstash a inner join cadastro_financeiro_itemcontabil b on concat(left(a.id_ic, 2), '.', substr(a.id_ic, 3)) = b.cod_item_contabil inner join clientes_clientes c on c.id = b.cliente_id order by cliente")	
    Clientes = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, cliente from painel_rateio_horas_por_ic_ativ_logstash a inner join cadastro_financeiro_itemcontabil b on concat(left(a.id_ic, 2), '.', substr(a.id_ic, 3)) = b.cod_item_contabil inner join clientes_clientes c on c.id = b.cliente_id order by cliente")
    Servicos = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, des_item_contabil from painel_rateio_horas_por_ic_ativ_logstash a inner join cadastro_financeiro_itemcontabil b on concat(left(a.id_ic, 2), '.', substr(a.id_ic, 3)) = b.cod_item_contabil inner join clientes_clientes c on c.id = b.cliente_id order by des_item_contabil")
    Descricoes = ResumoRateioHorasGns.objects.raw("SELECT id_tipo, descricao from painel_rateio_horas_por_ic_ativ_logstash a inner join cadastro_financeiro_itemcontabil b on concat(left(a.id_ic, 2), '.', substr(a.id_ic, 3)) = b.cod_item_contabil inner join clientes_clientes c on c.id = b.cliente_id order by des_item_contabil")	

    Detalhamento_horas_gns = ResumoRateioHorasGns.objects.raw("SELECT IFNULL(PESQ.id_tipo, '1') id_tipo, IFNULL(PESQ.cliente, PERI.cliente) cliente, IFNULL(PESQ.des_item_contabil, PERI.des_item_contabil) des_item_contabil,IFNULL(PESQ.descricao,  PERI.descricao) descricao, IFNULL(PESQ.qtd_horas, PERI.QTD)  qtd_horas, IFNULL(PESQ.periodo, PERI.PER) periodo FROM (SELECT rat.id_tipo, cli.cliente, cadf.des_item_contabil, rat.descricao, SUM(rat.qtd_horas )  qtd_horas, rat.periodo FROM painel_rateio_horas_por_ic_ativ_logstash rat INNER JOIN cadastro_financeiro_itemcontabil cadf ON CONCAT(LEFT(rat.id_ic, 2), '.', SUBSTR(rat.id_ic, 3)) = cadf.cod_item_contabil INNER JOIN clientes_clientes cli ON cli.id = cadf.cliente_id WHERE cliente = '%s' and des_item_contabil = '%s' group by rat.id_tipo, cli.cliente, cadf.des_item_contabil, rat.descricao, rat.periodo) PESQ RIGHT JOIN (SELECT * FROM(SELECT DISTINCT rat.id_tipo, cli.cliente, cadf.des_item_contabil, rat.descricao, 0 QTD FROM painel_rateio_horas_por_ic_ativ_logstash rat INNER JOIN cadastro_financeiro_itemcontabil cadf ON CONCAT(LEFT(rat.id_ic, 2), '.', SUBSTR(rat.id_ic, 3)) = cadf.cod_item_contabil INNER JOIN clientes_clientes cli ON cli.id = cadf.cliente_id where cliente = '%s' and des_item_contabil = '%s' ) DADOS, (SELECT CONCAT( DATE_FORMAT( DATE_ADD( NOW(), INTERVAL -1 MONTH), '%%Y%%m '), ' - ',  DATE_FORMAT(NOW(), '%%Y%%m ') ) PER UNION ALL SELECT CONCAT( DATE_FORMAT( DATE_ADD( NOW(), INTERVAL -2 MONTH), '%%Y%%m '), ' - ', DATE_FORMAT(DATE_ADD( NOW(), INTERVAL -1 MONTH), '%%Y%%m ') ) PER UNION ALL SELECT CONCAT( DATE_FORMAT( DATE_ADD( NOW(), INTERVAL -3 MONTH), '%%Y%%m '), ' - ',  DATE_FORMAT(DATE_ADD( NOW(), INTERVAL -2 MONTH), '%%Y%%m ') ) PER UNION ALL SELECT CONCAT( DATE_FORMAT( DATE_ADD( NOW(), INTERVAL -4 MONTH), '%%Y%%m '), ' - ',  DATE_FORMAT(DATE_ADD( NOW(), INTERVAL -3 MONTH), '%%Y%%m ') ) PER UNION ALL SELECT CONCAT( DATE_FORMAT( DATE_ADD( NOW(), INTERVAL -5 MONTH), '%%Y%%m '), ' - ',  DATE_FORMAT(DATE_ADD( NOW(), INTERVAL -4 MONTH), '%%Y%%m ') ) PER UNION ALL SELECT CONCAT(DATE_FORMAT( DATE_ADD( NOW(), INTERVAL -6 MONTH), '%%Y%%m '), ' - ',  DATE_FORMAT(DATE_ADD( NOW(), INTERVAL -5 MONTH), '%%Y%%m ') ) PER) PERIO) PERI ON PESQ.id_tipo = PERI.id_tipo AND PESQ.cliente = PERI.cliente AND PESQ.des_item_contabil = PERI.des_item_contabil AND PESQ.descricao = PERI.descricao AND PESQ.periodo = PERI.per ORDER BY descricao, periodo, cliente", [vCliente, vServico, vCliente, vServico]) 


    return render(request, 'painel_horas_gns/horasgns.html',
        {
         'data': data,    
         'resumoHorasGns': resumoHorasGns,
         'ResumoHorasGns' : ResumoHorasGns,
         'resumoHorasGnsProducao': resumoHorasGnsProducao,
         'resumoHorasGnsInterno': resumoHorasGnsInterno,
         'Detalhamento_horas_gns' : Detalhamento_horas_gns,
         'totalHoras': totalHoras,
         'periodos': periodos,
		 'Periodos' : Periodos,
         'Clientes' : Clientes,
         'Servicos' : Servicos,
	     'Descricoes' : Descricoes,
         'vPeriodo': vPeriodo,
         'vCliente' : vCliente,
         'vServico' : vServico,	 
#         'vDescricao' : vDescricao,		 
        })

def getDetalhamentoHrs (request):
    #vServico = request.GET[]
    detalhe_resumohrs = ResumoRateioHorasGns.objects.filter()
    return render(request, 'painel_horas_gns/horasgns_detalhe.html',
        {  
            'detalhe_resumohrs': detalhe_resumohrs,
        })
