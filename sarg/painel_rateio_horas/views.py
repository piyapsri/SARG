# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from painel_rateio_horas.models import RateioHoras
from django.db.models import Max

@login_required(login_url='/login')
def getRateioHoras(request):
    from datetime import datetime
    data = datetime.now()
    rateioHoras = RateioHoras.objects.raw("SELECT id_func,nome, CASE WHEN SEMANA_1 <> 'OK' THEN FN_FORMATA_HORA(semana_1 * 1, 'F') ELSE semana_1 END semana_1, CASE WHEN SEMANA_2 <> 'OK' THEN FN_FORMATA_HORA(semana_2 * 1, 'F') ELSE semana_2 END semana_2, CASE WHEN SEMANA_3 <> 'OK' THEN FN_FORMATA_HORA(semana_3 * 1, 'F') ELSE semana_3 END semana_3, CASE WHEN SEMANA_4 <> 'OK' THEN FN_FORMATA_HORA(semana_4 * 1, 'F') ELSE semana_4 END semana_4, CASE WHEN SEMANA_5 <> 'OK' THEN FN_FORMATA_HORA(semana_5 * 1, 'F') ELSE semana_5 END semana_5, estatus, periodo, ultima_semana_periodo FROM painel_rateio_horas_por_pessoa_logstash ORDER BY nome")
    amount_success = RateioHoras.objects.filter(estatus = 'RATEADO').count()
    amount_warning = RateioHoras.objects.filter(estatus = 'PENDENTE').count()
    amount_danger = RateioHoras.objects.filter(estatus = 'ATRASADO').count()
    ultima_semana_periodo = RateioHoras.objects.values_list('ultima_semana_periodo', flat=True).first()
    loop_times = range(1, ultima_semana_periodo + 1)
    return render(request, 'painel_rateio_horas/rateio.html',
        {
         'data': data,    
         'rateioHoras': rateioHoras,
         'amount_success': amount_success,
         'amount_warning': amount_warning,
         'amount_danger': amount_danger,
         'ultima_semana_periodo': ultima_semana_periodo,
         'loop_times':loop_times,
        })

       
