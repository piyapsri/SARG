# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Max

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Value, Q
from painel_ongoing.models import ongoing

@login_required(login_url='/login')
def ShowOngoing(request):
    from datetime import datetime
    res = ongoing.objects.filter().aggregate(max_per=Max('periodo'))
    vPeriodo = request.POST.get('periodo', res.get('max_per'))

    data = datetime.now()
    #horas_ongoing = ongoing.objects.all()
    #horas_ongoing = ongoing.objects.raw("select o.descricao_item_contabil, o.item_contabil, sum(o.hora_normal) hora_normal, sum(o.hora_75_pc) hora_75_pc, sum(o.hora_100_pc) hora_100_pc, sum(o.hora_total) hora_total from painel_ongoing_ongoing o inner join cadastro_financeiro_itemcontabil ic on ic.cod_item_contabil = o.item_contabil where ic.cod_tipo_item_contabil = 'GNS' group by o.descricao_item_contabil, o.item_contabil order by o.descricao_item_contabil")
    horas_ongoing = ongoing.objects.raw("SELECT o.periodo, ic.des_item_contabil, o.item_contabil, SUM(o.hora_normal) hora_normal, SUM(o.hora_75_pc) hora_75_pc, SUM(o.hora_100_pc) hora_100_pc, SUM(o.hora_total) hora_total FROM painel_ongoing_ongoing o INNER JOIN cadastro_financeiro_itemcontabil ic ON ic.cod_item_contabil = o.item_contabil INNER JOIN cadastro_financeiro_atividade ac ON ic.id = ac.cod_item_contabil_id AND ac.cod_atividade = o.cod_atividade WHERE ic.cod_tipo_item_contabil = 'GNS' AND o.periodo = '%s' GROUP BY o.periodo , ic.des_item_contabil , o.item_contabil ORDER BY o.item_contabil, ic.des_item_contabil" % vPeriodo)
    periodos = ongoing.objects.raw("SELECT p.periodo, max(p.item_contabil) item_contabil FROM painel_ongoing_ongoing p GROUP BY p.periodo ORDER BY p.periodo DESC")
    return render(request, 'painel_ongoing/ongoing.html',
        {
            'data': data,
            'horas_ongoing': horas_ongoing,
            'periodos': periodos,
            'vPeriodo': vPeriodo,
        })
    