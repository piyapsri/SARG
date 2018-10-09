# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from painel_oportunidades.models import OPORTUNIDADES, HORAS_OPORTUNIDADES

@login_required(login_url='/login')
def ShowOportunities(request):
    from datetime import datetime
    data = datetime.now()	
    Oportunities = OPORTUNIDADES.objects.all()
    amount_oportunidades = OPORTUNIDADES.objects.exclude(status='Finalizada').count()
    amount_oportunidadesEnv = OPORTUNIDADES.objects.filter(status='Proposta Enviada').count()	
    amount_oportunidadesDes = OPORTUNIDADES.objects.filter(status='Desenvolvimento de Proposta').count()
    amount_oportunidadesPros = OPORTUNIDADES.objects.filter(status='Prospecção de novos negócios').count()
	
    horas_realizadas = HORAS_OPORTUNIDADES.objects.raw("SELECT id, item_contabil, SUM(hora_total) hora_total FROM (SELECT DISTINCT p.id, ic.cod_item_contabil item_contabil, IFNULL((SELECT  SUM(horas_arrend) hora_total FROM painel_projetos_e_oportunidaes_ic_x_horas_logstash WHERE item_contabil = ic.cod_item_contabil AND cod_atividade = ativ.cod_atividade), 0) hora_total FROM painel_oportunidades_oportunidades p INNER JOIN clientes_clientes cli ON p.cliente_id = cli.id INNER JOIN cadastro_financeiro_itemcontabil ic ON p.item_contabil_id = ic.id INNER JOIN painel_oportunidades_oportunidades_codigo_atividade pativ ON p.id = pativ.oportunidades_id LEFT JOIN cadastro_financeiro_atividade ativ ON pativ.atividade_id = ativ.id AND p.item_contabil_id = ativ.cod_item_contabil_id) HORAS GROUP BY id, item_contabil")

	
    return render(request, 'painel_oportunidades/oportunidades.html',
        {
         'Oportunities': Oportunities,
         'horas_realizadas': horas_realizadas,
		 'amount_oportunidades': amount_oportunidades,
		 'amount_oportunidadesEnv': amount_oportunidadesEnv,
		 'amount_oportunidadesDes': amount_oportunidadesDes,
		 'amount_oportunidadesPros': amount_oportunidadesPros,
			'data': data,
        })
def ShowOportunities_tv(request):
    from datetime import datetime
    data = datetime.now()
    #Oportunities = OPORTUNIDADES.objects.all()    
    Oportunities = OPORTUNIDADES.objects.filter(id__in=[20,3,4,5,6])
    return render(request, 'painel_oportunidades/oportunidades_tv.html',
        {
         'Oportunities': Oportunities,
         'data': data,
        })

def ShowOportunities2_tv(request):
    from datetime import datetime
    data = datetime.now()
    #Oportunities = OPORTUNIDADES.objects.all()
    Oportunities = OPORTUNIDADES.objects.filter(id__in=[7,17,21,18,22])
    return render(request, 'painel_oportunidades/oportunidades2_tv.html',
        {
         'Oportunities': Oportunities,
         'data': data,
        })

def ShowOportunities3_tv(request):
    from datetime import datetime
    data = datetime.now()
    #Oportunities = OPORTUNIDADES.objects.all()
    Oportunities = OPORTUNIDADES.objects.filter(id__in=[14,15])
    return render(request, 'painel_oportunidades/oportunidades3_tv.html',
        {
         'Oportunities': Oportunities,
         'data': data,
        })
