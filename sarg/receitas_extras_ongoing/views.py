from django.shortcuts import render

# Create your views here.

from receitas_extras_ongoing.models import ReceitasExtrasOngoing, receitas_extras_ongoing_operadoras
from clientes.models import Clientes

def ShowReceitasExtrasOngoing(request):
    import datetime
    data = datetime.datetime.now()
    d = datetime.date.today()
    ano_corrente = d.strftime('%Y')
    #receitas_extras_ongoing=ReceitasExtrasOngoing.objects.values()
#    receitas_extras_ongoing = ReceitasExtrasOngoing.objects.raw("SELECT 1 as id, concat(YEAR(data), MONTH(data)) ano_mes, sum(valor_orcado) valor_total from receitas_extras_ongoing_receitasextrasongoing group by ano_mes order by ano_mes asc")
    receitas_extras_ongoing = ReceitasExtrasOngoing.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL(VALOR_ORCADO, 0) VALOR_ORCADO, IFNULL(VALOR_ACUMULADO, 0) VALOR_ACUMULADO FROM (SELECT  DADOS.ANOMES AS ANOMES, SUM(IFNULL(VALOR_ORCADO, 0)) AS VALOR_ORCADO, SUM(@VALOR_ACUMULADO:=@VALOR_ACUMULADO + IFNULL(VALOR_ORCADO, 0)) AS VALOR_ACUMULADO FROM (SELECT DATE_FORMAT(data,'%%Y%%m') ANOMES, SUM(IFNULL(ORC.valor_orcado, 0)) AS VALOR_ORCADO FROM receitas_extras_ongoing_receitasextrasongoing ORC where YEAR(data) = YEAR(curdate())  GROUP BY 1) AS DADOS JOIN (SELECT @VALOR_ACUMULADO:=0) vp GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")
#    receitas_extras_por_operadora = ReceitasExtrasOngoing.objects.raw("select 1 as id, concat(YEAR(a.data), MONTH(a.data)) ano_mes, sum(a.valor_orcado) valor_total, b.cliente cliente from receitas_extras_ongoing_receitasextrasongoing a inner join clientes_clientes b on a.cliente_id=b.id group by ano_mes, cliente order by ano_mes")
    receitas_extras_por_operadora = ReceitasExtrasOngoing.objects.all()
    meses_receitas_extras_por_operadora = receitas_extras_ongoing_operadoras.objects.filter(ano_mes__contains=ano_corrente).values('ano_mes').order_by('ano_mes').distinct()
    A = receitas_extras_ongoing_operadoras.objects.all()
    A_OI = receitas_extras_ongoing_operadoras.objects.filter(cliente='Oi', ano_mes__contains=ano_corrente).values()
    A_VIVO = receitas_extras_ongoing_operadoras.objects.filter(cliente='VIVO', ano_mes__contains=ano_corrente).values() 
    saldo_horas = ReceitasExtrasOngoing.objects.raw("select 1 as id, concat(YEAR(data) , LPAD(MONTH(data),2,'0')) ano_mes, sum(horas_orcadas) horas_orcadas from receitas_extras_ongoing_receitasextrasongoing where YEAR(data) = YEAR(curdate()) group by ano_mes")
 #   saldo_horas_oi = ReceitasExtrasOngoing.objects.raw("select 1 as id, concat(YEAR(a.data), MONTH(a.data)) ano_mes, sum(a.horas_orcadas) horas_orcadas, b.cliente cliente from receitas_extras_ongoing_receitasextrasongoing a inner join clientes_clientes b on a.cliente_id=b.id where b.cliente = 'oi' group by ano_mes, cliente order by ano_mes")
 #   saldo_horas_vivo = ReceitasExtrasOngoing.objects.raw("select 1 as id, concat(YEAR(a.data), MONTH(a.data)) ano_mes, sum(a.horas_orcadas) horas_orcadas, b.cliente cliente from receitas_extras_ongoing_receitasextrasongoing a inner join clientes_clientes b on a.cliente_id=b.id where b.cliente = 'vivo' group by ano_mes, cliente order by ano_mes")	
	
    return render(request, 'receitas_extras_ongoing/receitas_extras_ongoing.html',
        {
         'data': data,		
         'receitas_extras_ongoing': receitas_extras_ongoing,
			'receitas_extras_por_operadora': receitas_extras_por_operadora,
			'A': A,
			'A_OI': A_OI,			
			'A_VIVO': A_VIVO,		
			'saldo_horas': saldo_horas,
#			'saldo_horas_oi': saldo_horas_oi,
#			'saldo_horas_vivo': saldo_horas_vivo,
			'meses_receitas_extras_por_operadora': meses_receitas_extras_por_operadora,
        })

