# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

from painel_projetos.models import PROJETOS, HORAS_ONGOING
#from painel_ongoing.models import ongoing
#item_contabil, descricao_item_contabil, cod_atividade, des_atividade
@login_required(login_url='/login')
def ShowProjects(request):
    from datetime import datetime
    data = datetime.now()
    Projects = PROJETOS.objects.all()
    amount_projetos = PROJETOS.objects.filter(status__in=[1,2,3,4]).count()
    amount_projetosOK = PROJETOS.objects.filter(status='1').count()
    amount_projetosAte = PROJETOS.objects.filter(status='2').count()
    amount_projetosPau = PROJETOS.objects.filter(status='4').count()
    amount_projetosPro = PROJETOS.objects.filter(status='3').count()
    horas_ongoing = HORAS_ONGOING.objects.raw("select id, item_contabil, sum(hora_total) hora_total from ( SELECT DISTINCT p.id, ic.cod_item_contabil item_contabil, IFNULL((SELECT  SUM(horas_arrend) hora_total FROM painel_projetos_e_oportunidaes_ic_x_horas_logstash WHERE item_contabil = ic.cod_item_contabil AND cod_atividade = ativ.cod_atividade), 0) hora_total FROM painel_projetos_projetos p INNER JOIN clientes_clientes cli ON p.cliente_id = cli.id INNER JOIN cadastro_financeiro_itemcontabil ic ON p.item_contabil_id = ic.id INNER JOIN painel_projetos_projetos_codigo_atividade pativ ON p.id = pativ.projetos_id LEFT JOIN cadastro_financeiro_atividade ativ ON pativ.atividade_id = ativ.id AND p.item_contabil_id = ativ.cod_item_contabil_id ) HORAS GROUP BY id, item_contabil")
    return render(request, 'painel_projetos/projetos.html',
        {
			'amount_projetos': amount_projetos,
            'amount_projetosOK': amount_projetosOK,
			'amount_projetosAte': amount_projetosAte,
			'amount_projetosPau': amount_projetosPau,
			'amount_projetosPro': amount_projetosPro,
			
            'Projects': Projects,			
            'data': data,
            'horas_ongoing': horas_ongoing,					
        })

def ShowProjects_tv(request):
    from datetime import datetime
    data = datetime.now()
    Projects = PROJETOS.objects.all().order_by('-data_inicio')
    return render(request, 'painel_projetos/projetos_tv.html',
        {
            'Projects': Projects,
            'data': data,
        })

def ShowProjects2_tv(request):
    from datetime import datetime
    data = datetime.now()
    Projects = PROJETOS.objects.all().order_by('-data_inicio')
    return render(request, 'painel_projetos/projetos2_tv.html',
        {
            'Projects': Projects,
            'data': data,
        })

def ShowProjects3_tv(request):
    from datetime import datetime
    data = datetime.now()
    Projects = PROJETOS.objects.all().order_by('-data_inicio')
    return render(request, 'painel_projetos/projetos3_tv.html',
        {
            'Projects': Projects,
            'data': data,
        })

