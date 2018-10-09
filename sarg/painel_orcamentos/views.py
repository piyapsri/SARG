# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from painel_orcamentos.models import PainelOrcamentosLogstash, OrcamentosAcumulado, ORCAMENTOS, ORCAMENTOS_PORCENTAGEM_BEN, ORCAMENTOS_PORCENTAGEM_CAP, ORCAMENTOS_PORCENTAGEM_CON, ORCAMENTOS_PORCENTAGEM_EVE, ORCAMENTOS_PORCENTAGEM_FOR, ORCAMENTOS_PORCENTAGEM_VIG, ORCAMENTOS_PORCENTAGEM_SEM
from django.db.models import Sum
#import numpy as np
from itertools import accumulate
	
@login_required(login_url='/login')
@permission_required('p', raise_exception=True)
def ShowOrcamentos(request):
    import datetime
    data = datetime.datetime.now()
    d = datetime.date.today()
    ano_corrente = d.strftime('%Y')
    mes_corrente = d.strftime('%m')
    ano_mes_corrente = d.strftime('%Y%m')


#### Legendas ####

# ORC - Orçamento
# TOT - Total
# PRE - Previsto
# REL - Realizado
# BEN - Benefício
# CAP - Capacitação
# CON - Consumo
# EVE - Evento
# FOR - Fornecedor
# VIG - Viagem
# SEM - Sem Classificação

#### /Legendas ####

# Valores Dinamicos
#   Orcamentos_Previstos = ORCAMENTOS.objects.raw("select a.id, a.despesa, a.mes, a.ano, a.valor,(select c.total from (select b.despesa, b.ano, sum(b.valor) as total from painel_orcamentos_orcamentos b group by b.despesa, b.ano) c where a.despesa = c.despesa and a.ano = c.ano) total_ano from painel_orcamentos_orcamentos a where a.mes = %s and a.ano = %s", [mes_corrente, ano_corrente])	


# Valores de Benefício:
	
    ORC_BEN_PRE_MES = ORCAMENTOS.objects.filter(despesa='Beneficios', mes=mes_corrente, ano=ano_corrente).values_list('valor', flat=True).first()
    ORC_BEN_PRE_ANO = ORCAMENTOS.objects.filter(despesa='Beneficios', ano=ano_corrente).aggregate(Sum('valor'))['valor__sum']

    ORC_BEN_REL_PER = ORCAMENTOS_PORCENTAGEM_BEN.objects.using('monitorcs').filter(tipo_despesa='BENEFICIOS').values('descricao_natureza', 'perc')
    ORC_BEN_HIST_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, grupo_despesa='BENEFICIOS').values('periodo', 'grupo_despesa').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')
    ORC_BEN_PRE_ANO_ACU = OrcamentosAcumulado.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL((VALOR_PREVISTO - VALOR_APROVADO), 0) VALOR_SALDO, IFNULL(VALOR_APROVADO, 0) VALOR_APROVADO, IFNULL(VALOR_PREVISTO, 0) VALOR_PREVISTO, IFNULL(VALOR_PROJETADO, 0) VALOR_PROJETADO FROM (SELECT  MESES.ANOMES AS ANOMES, SUM(@VALOR_APROVADO:=@VALOR_APROVADO + IFNULL(VALOR_APROVADO, 0)) VALOR_APROVADO, SUM(@VALOR_PREVISTO:=@VALOR_PREVISTO + IFNULL(VALOR_PREVISTO, 0)) AS VALOR_PREVISTO, SUM(@VALOR_PROJETADO:=@VALOR_PROJETADO + IFNULL(VALOR_PROJETADO, 0)) AS VALOR_PROJETADO FROM (SELECT CONCAT(YEAR(CURDATE()), '01') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '02') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '03') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '04') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '05') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '06') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '07') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '08') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '09') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '10') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '11') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '12') AS ANOMES) AS MESES LEFT JOIN (SELECT DISTINCT TMP2.PERIODO, TMP2.DESPESA, MAX(TMP2.VALOR_APROVADO) VALOR_APROVADO, MAX(TMP2.VALOR_PREVISTO) VALOR_PREVISTO, MAX(TMP2.VALOR_PROJETADO) VALOR_PROJETADO FROM ( SELECT  ORC.PERIODO AS PERIODO, UPPER(ORC.grupo_despesa) AS DESPESA, SUM(IFNULL(ORC.valor_aprovado, 0)) AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_logstash ORC GROUP BY 1 , 2  UNION ALL  SELECT  CONCAT(ORC2.ANO, ORC2.MES) AS PERIODO, UPPER(ORC2.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, SUM(IFNULL(ORC2.valor, 0)) AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC2 GROUP BY 1 , 2 UNION ALL SELECT  CONCAT(ORC3.ANO, ORC3.MES) AS PERIODO, UPPER(ORC3.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, SUM(IFNULL(ORC3.valor_projetado, 0)) AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC3 GROUP BY 1 , 2 ) AS TMP2 WHERE UPPER(TMP2.DESPESA) = 'BENEFICIOS' GROUP BY 1 , 2) AS TMP3 ON MESES.ANOMES = TMP3.PERIODO JOIN (SELECT @VALOR_APROVADO:=0) va JOIN (SELECT @VALOR_PREVISTO:=0) vp JOIN (SELECT @VALOR_PROJETADO:=0) vr GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")
	#.filter(grupo_despesa='BENEFICIOS', periodo__contains=ano_corrente).order_by('periodo').values()
	
    TOT_ORC_BEN_REL_MES = PainelOrcamentosLogstash.objects.filter(grupo_despesa='BENEFICIOS', periodo=ano_mes_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
    TOT_ORC_BEN_REL_ANO = PainelOrcamentosLogstash.objects.filter(grupo_despesa='BENEFICIOS', periodo__contains=ano_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']

# Valores de Capacitação:	

    ORC_CAP_PRE_MES = ORCAMENTOS.objects.filter(despesa='Capacitacoes', mes=mes_corrente, ano=ano_corrente).values_list('valor', flat=True).first()
    ORC_CAP_PRE_ANO = ORCAMENTOS.objects.filter(despesa='Capacitacoes', ano=ano_corrente).aggregate(Sum('valor'))['valor__sum']

    ORC_CAP_REL_PER = ORCAMENTOS_PORCENTAGEM_CAP.objects.using('monitorcs').filter(tipo_despesa='DESPESAS C/ CAPACITACAO').values('descricao_natureza', 'perc')
    ORC_CAP_HIST_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, grupo_despesa='CAPACITACOES').values('periodo', 'grupo_despesa').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')		
#    ORC_CAP_PRE_ANO_ACU = ORCAMENTOS.objects.filter(despesa='Capacitacoes', ano=ano_corrente).values()
    ORC_CAP_PRE_ANO_ACU = OrcamentosAcumulado.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL((VALOR_PREVISTO - VALOR_APROVADO), 0) VALOR_SALDO, IFNULL(VALOR_APROVADO, 0) VALOR_APROVADO, IFNULL(VALOR_PREVISTO, 0) VALOR_PREVISTO, IFNULL(VALOR_PROJETADO, 0) VALOR_PROJETADO FROM (SELECT  MESES.ANOMES AS ANOMES, SUM(@VALOR_APROVADO:=@VALOR_APROVADO + IFNULL(VALOR_APROVADO, 0)) VALOR_APROVADO, SUM(@VALOR_PREVISTO:=@VALOR_PREVISTO + IFNULL(VALOR_PREVISTO, 0)) AS VALOR_PREVISTO, SUM(@VALOR_PROJETADO:=@VALOR_PROJETADO + IFNULL(VALOR_PROJETADO, 0)) AS VALOR_PROJETADO FROM (SELECT CONCAT(YEAR(CURDATE()), '01') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '02') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '03') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '04') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '05') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '06') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '07') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '08') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '09') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '10') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '11') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '12') AS ANOMES) AS MESES LEFT JOIN (SELECT DISTINCT TMP2.PERIODO, TMP2.DESPESA, MAX(TMP2.VALOR_APROVADO) VALOR_APROVADO, MAX(TMP2.VALOR_PREVISTO) VALOR_PREVISTO, MAX(TMP2.VALOR_PROJETADO) VALOR_PROJETADO FROM ( SELECT  ORC.PERIODO AS PERIODO, UPPER(ORC.grupo_despesa) AS DESPESA, SUM(IFNULL(ORC.valor_aprovado, 0)) AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_logstash ORC GROUP BY 1 , 2  UNION ALL  SELECT  CONCAT(ORC2.ANO, ORC2.MES) AS PERIODO, UPPER(ORC2.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, SUM(IFNULL(ORC2.valor, 0)) AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC2 GROUP BY 1 , 2 UNION ALL SELECT  CONCAT(ORC3.ANO, ORC3.MES) AS PERIODO, UPPER(ORC3.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, SUM(IFNULL(ORC3.valor_projetado, 0)) AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC3 GROUP BY 1 , 2 ) AS TMP2 WHERE UPPER(TMP2.DESPESA) = 'CAPACITACOES' GROUP BY 1 , 2) AS TMP3 ON MESES.ANOMES = TMP3.PERIODO JOIN (SELECT @VALOR_APROVADO:=0) va JOIN (SELECT @VALOR_PREVISTO:=0) vp JOIN (SELECT @VALOR_PROJETADO:=0) vr GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")
	
    TOT_ORC_CAP_REL_MES = PainelOrcamentosLogstash.objects.filter(grupo_despesa='CAPACITACOES', periodo=ano_mes_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
    TOT_ORC_CAP_REL_ANO = PainelOrcamentosLogstash.objects.filter(grupo_despesa='CAPACITACOES', periodo__contains=ano_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']

# Valores de Consumo:	
	
    ORC_CON_PRE_MES = ORCAMENTOS.objects.filter(despesa='Consumos', mes=mes_corrente, ano=ano_corrente).values_list('valor', flat=True).first()
    ORC_CON_PRE_ANO = ORCAMENTOS.objects.filter(despesa='Consumos', ano=ano_corrente).aggregate(Sum('valor'))['valor__sum']

    ORC_CON_REL_PER = ORCAMENTOS_PORCENTAGEM_CON.objects.using('monitorcs').filter(tipo_despesa='DESPESAS DE CONSUMO').values('descricao_natureza', 'perc')
    ORC_CON_HIST_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, grupo_despesa='CONSUMO').values('periodo', 'grupo_despesa').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')		
#    ORC_CON_PRE_ANO_ACU = ORCAMENTOS.objects.filter(despesa='Consumos', ano=ano_corrente).values()		
    ORC_CON_PRE_ANO_ACU = OrcamentosAcumulado.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL((VALOR_PREVISTO - VALOR_APROVADO), 0) VALOR_SALDO, IFNULL(VALOR_APROVADO, 0) VALOR_APROVADO, IFNULL(VALOR_PREVISTO, 0) VALOR_PREVISTO, IFNULL(VALOR_PROJETADO, 0) VALOR_PROJETADO FROM (SELECT  MESES.ANOMES AS ANOMES, SUM(@VALOR_APROVADO:=@VALOR_APROVADO + IFNULL(VALOR_APROVADO, 0)) VALOR_APROVADO, SUM(@VALOR_PREVISTO:=@VALOR_PREVISTO + IFNULL(VALOR_PREVISTO, 0)) AS VALOR_PREVISTO, SUM(@VALOR_PROJETADO:=@VALOR_PROJETADO + IFNULL(VALOR_PROJETADO, 0)) AS VALOR_PROJETADO FROM (SELECT CONCAT(YEAR(CURDATE()), '01') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '02') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '03') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '04') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '05') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '06') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '07') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '08') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '09') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '10') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '11') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '12') AS ANOMES) AS MESES LEFT JOIN (SELECT DISTINCT TMP2.PERIODO, TMP2.DESPESA, MAX(TMP2.VALOR_APROVADO) VALOR_APROVADO, MAX(TMP2.VALOR_PREVISTO) VALOR_PREVISTO, MAX(TMP2.VALOR_PROJETADO) VALOR_PROJETADO FROM ( SELECT  ORC.PERIODO AS PERIODO, UPPER(ORC.grupo_despesa) AS DESPESA, SUM(IFNULL(ORC.valor_aprovado, 0)) AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_logstash ORC GROUP BY 1 , 2  UNION ALL  SELECT  CONCAT(ORC2.ANO, ORC2.MES) AS PERIODO, UPPER(ORC2.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, SUM(IFNULL(ORC2.valor, 0)) AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC2 GROUP BY 1 , 2 UNION ALL SELECT  CONCAT(ORC3.ANO, ORC3.MES) AS PERIODO, UPPER(ORC3.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, SUM(IFNULL(ORC3.valor_projetado, 0)) AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC3 GROUP BY 1 , 2 ) AS TMP2 WHERE UPPER(TMP2.DESPESA) = 'CONSUMO' GROUP BY 1 , 2) AS TMP3 ON MESES.ANOMES = TMP3.PERIODO JOIN (SELECT @VALOR_APROVADO:=0) va JOIN (SELECT @VALOR_PREVISTO:=0) vp JOIN (SELECT @VALOR_PROJETADO:=0) vr GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")
	
    TOT_ORC_CON_REL_MES = PainelOrcamentosLogstash.objects.filter(grupo_despesa='CONSUMO', periodo=ano_mes_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
    TOT_ORC_CON_REL_ANO = PainelOrcamentosLogstash.objects.filter(grupo_despesa='CONSUMO', periodo__contains=ano_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	

# Valores Eventos

    ORC_EVE_PRE_MES = ORCAMENTOS.objects.filter(despesa='Eventos', mes=mes_corrente, ano=ano_corrente).values_list('valor', flat=True).first()
    ORC_EVE_PRE_ANO = ORCAMENTOS.objects.filter(despesa='Eventos', ano=ano_corrente).aggregate(Sum('valor'))['valor__sum']

    ORC_EVE_REL_PER = ORCAMENTOS_PORCENTAGEM_EVE.objects.using('monitorcs').filter(tipo_despesa='EVENTOS').values('descricao_natureza', 'perc')
    ORC_EVE_HIST_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, grupo_despesa='EVENTOS').values('periodo', 'grupo_despesa').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')		
#    ORC_EVE_PRE_ANO_ACU = ORCAMENTOS.objects.filter(despesa='Eventos', ano=ano_corrente).values()		
    ORC_EVE_PRE_ANO_ACU = OrcamentosAcumulado.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL((VALOR_PREVISTO - VALOR_APROVADO), 0) VALOR_SALDO, IFNULL(VALOR_APROVADO, 0) VALOR_APROVADO, IFNULL(VALOR_PREVISTO, 0) VALOR_PREVISTO, IFNULL(VALOR_PROJETADO, 0) VALOR_PROJETADO FROM (SELECT  MESES.ANOMES AS ANOMES, SUM(@VALOR_APROVADO:=@VALOR_APROVADO + IFNULL(VALOR_APROVADO, 0)) VALOR_APROVADO, SUM(@VALOR_PREVISTO:=@VALOR_PREVISTO + IFNULL(VALOR_PREVISTO, 0)) AS VALOR_PREVISTO, SUM(@VALOR_PROJETADO:=@VALOR_PROJETADO + IFNULL(VALOR_PROJETADO, 0)) AS VALOR_PROJETADO FROM (SELECT CONCAT(YEAR(CURDATE()), '01') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '02') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '03') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '04') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '05') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '06') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '07') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '08') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '09') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '10') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '11') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '12') AS ANOMES) AS MESES LEFT JOIN (SELECT DISTINCT TMP2.PERIODO, TMP2.DESPESA, MAX(TMP2.VALOR_APROVADO) VALOR_APROVADO, MAX(TMP2.VALOR_PREVISTO) VALOR_PREVISTO, MAX(TMP2.VALOR_PROJETADO) VALOR_PROJETADO FROM ( SELECT  ORC.PERIODO AS PERIODO, UPPER(ORC.grupo_despesa) AS DESPESA, SUM(IFNULL(ORC.valor_aprovado, 0)) AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_logstash ORC GROUP BY 1 , 2  UNION ALL  SELECT  CONCAT(ORC2.ANO, ORC2.MES) AS PERIODO, UPPER(ORC2.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, SUM(IFNULL(ORC2.valor, 0)) AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC2 GROUP BY 1 , 2 UNION ALL SELECT  CONCAT(ORC3.ANO, ORC3.MES) AS PERIODO, UPPER(ORC3.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, SUM(IFNULL(ORC3.valor_projetado, 0)) AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC3 GROUP BY 1 , 2 ) AS TMP2 WHERE UPPER(TMP2.DESPESA) = 'EVENTOS' GROUP BY 1 , 2) AS TMP3 ON MESES.ANOMES = TMP3.PERIODO JOIN (SELECT @VALOR_APROVADO:=0) va JOIN (SELECT @VALOR_PREVISTO:=0) vp JOIN (SELECT @VALOR_PROJETADO:=0) vr GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")

	
    TOT_ORC_EVE_REL_MES = PainelOrcamentosLogstash.objects.filter(grupo_despesa='EVENTOS', periodo=ano_mes_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
    TOT_ORC_EVE_REL_ANO = PainelOrcamentosLogstash.objects.filter(grupo_despesa='EVENTOS', periodo__contains=ano_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']		


# Valores Fornecedores	

    ORC_FOR_PRE_MES = ORCAMENTOS.objects.filter(despesa='Fornecedores', mes=mes_corrente, ano=ano_corrente).values_list('valor', flat=True).first()
    ORC_FOR_PRE_ANO = ORCAMENTOS.objects.filter(despesa='Fornecedores', ano=ano_corrente).aggregate(Sum('valor'))['valor__sum']
    
    ORC_FOR_REL_PER = ORCAMENTOS_PORCENTAGEM_FOR.objects.using('monitorcs').filter(tipo_despesa='FORNECEDORES').values('descricao_natureza', 'perc')
    ORC_FOR_HIST_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, grupo_despesa='FORNECEDORES').values('periodo', 'grupo_despesa').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')	
#    ORC_FOR_PRE_ANO_ACU = ORCAMENTOS.objects.filter(despesa='Fornecedores', ano=ano_corrente).values()	
    ORC_FOR_PRE_ANO_ACU = OrcamentosAcumulado.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL((VALOR_PREVISTO - VALOR_APROVADO), 0) VALOR_SALDO, IFNULL(VALOR_APROVADO, 0) VALOR_APROVADO, IFNULL(VALOR_PREVISTO, 0) VALOR_PREVISTO, IFNULL(VALOR_PROJETADO, 0) VALOR_PROJETADO FROM (SELECT  MESES.ANOMES AS ANOMES, SUM(@VALOR_APROVADO:=@VALOR_APROVADO + IFNULL(VALOR_APROVADO, 0)) VALOR_APROVADO, SUM(@VALOR_PREVISTO:=@VALOR_PREVISTO + IFNULL(VALOR_PREVISTO, 0)) AS VALOR_PREVISTO, SUM(@VALOR_PROJETADO:=@VALOR_PROJETADO + IFNULL(VALOR_PROJETADO, 0)) AS VALOR_PROJETADO FROM (SELECT CONCAT(YEAR(CURDATE()), '01') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '02') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '03') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '04') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '05') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '06') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '07') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '08') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '09') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '10') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '11') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '12') AS ANOMES) AS MESES LEFT JOIN (SELECT DISTINCT TMP2.PERIODO, TMP2.DESPESA, MAX(TMP2.VALOR_APROVADO) VALOR_APROVADO, MAX(TMP2.VALOR_PREVISTO) VALOR_PREVISTO, MAX(TMP2.VALOR_PROJETADO) VALOR_PROJETADO FROM ( SELECT  ORC.PERIODO AS PERIODO, UPPER(ORC.grupo_despesa) AS DESPESA, SUM(IFNULL(ORC.valor_aprovado, 0)) AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_logstash ORC GROUP BY 1 , 2  UNION ALL  SELECT  CONCAT(ORC2.ANO, ORC2.MES) AS PERIODO, UPPER(ORC2.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, SUM(IFNULL(ORC2.valor, 0)) AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC2 GROUP BY 1 , 2 UNION ALL SELECT  CONCAT(ORC3.ANO, ORC3.MES) AS PERIODO, UPPER(ORC3.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, SUM(IFNULL(ORC3.valor_projetado, 0)) AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC3 GROUP BY 1 , 2 ) AS TMP2 WHERE UPPER(TMP2.DESPESA) = 'FORNECEDORES' GROUP BY 1 , 2) AS TMP3 ON MESES.ANOMES = TMP3.PERIODO JOIN (SELECT @VALOR_APROVADO:=0) va JOIN (SELECT @VALOR_PREVISTO:=0) vp JOIN (SELECT @VALOR_PROJETADO:=0) vr GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")
	

    TOT_ORC_FOR_REL_MES = PainelOrcamentosLogstash.objects.filter(grupo_despesa='FORNECEDORES', periodo=ano_mes_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
    TOT_ORC_FOR_REL_ANO = PainelOrcamentosLogstash.objects.filter(grupo_despesa='FORNECEDORES', periodo__contains=ano_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']		

# Valores Viagens

    ORC_VIG_PRE_MES = ORCAMENTOS.objects.filter(despesa='Viagens', mes=mes_corrente, ano=ano_corrente).values_list('valor', flat=True).first()
    ORC_VIG_PRE_ANO = ORCAMENTOS.objects.filter(despesa='Viagens', ano=ano_corrente).aggregate(Sum('valor'))['valor__sum']

    ORC_VIG_REL_PER = ORCAMENTOS_PORCENTAGEM_VIG.objects.using('monitorcs').filter(tipo_despesa='DESPESAS C/ VIAGENS').values('descricao_natureza', 'perc')
	
    ORC_VIG_HIST_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, grupo_despesa='VIAGENS').values('periodo', 'grupo_despesa').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')

#    ORC_VIG_PRE_ANO_ACU = ORCAMENTOS.objects.filter(despesa='Viagens', ano=ano_corrente).values()	
    ORC_VIG_PRE_ANO_ACU = OrcamentosAcumulado.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL((VALOR_PREVISTO - VALOR_APROVADO), 0) VALOR_SALDO, IFNULL(VALOR_APROVADO, 0) VALOR_APROVADO, IFNULL(VALOR_PREVISTO, 0) VALOR_PREVISTO, IFNULL(VALOR_PROJETADO, 0) VALOR_PROJETADO FROM (SELECT  MESES.ANOMES AS ANOMES, SUM(@VALOR_APROVADO:=@VALOR_APROVADO + IFNULL(VALOR_APROVADO, 0)) VALOR_APROVADO, SUM(@VALOR_PREVISTO:=@VALOR_PREVISTO + IFNULL(VALOR_PREVISTO, 0)) AS VALOR_PREVISTO, SUM(@VALOR_PROJETADO:=@VALOR_PROJETADO + IFNULL(VALOR_PROJETADO, 0)) AS VALOR_PROJETADO FROM (SELECT CONCAT(YEAR(CURDATE()), '01') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '02') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '03') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '04') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '05') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '06') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '07') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '08') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '09') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '10') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '11') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '12') AS ANOMES) AS MESES LEFT JOIN (SELECT DISTINCT TMP2.PERIODO, TMP2.DESPESA, MAX(TMP2.VALOR_APROVADO) VALOR_APROVADO, MAX(TMP2.VALOR_PREVISTO) VALOR_PREVISTO, MAX(TMP2.VALOR_PROJETADO) VALOR_PROJETADO FROM ( SELECT  ORC.PERIODO AS PERIODO, UPPER(ORC.grupo_despesa) AS DESPESA, SUM(IFNULL(ORC.valor_aprovado, 0)) AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_logstash ORC GROUP BY 1 , 2  UNION ALL  SELECT  CONCAT(ORC2.ANO, ORC2.MES) AS PERIODO, UPPER(ORC2.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, SUM(IFNULL(ORC2.valor, 0)) AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC2 GROUP BY 1 , 2 UNION ALL SELECT  CONCAT(ORC3.ANO, ORC3.MES) AS PERIODO, UPPER(ORC3.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, SUM(IFNULL(ORC3.valor_projetado, 0)) AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC3 GROUP BY 1 , 2 ) AS TMP2 WHERE UPPER(TMP2.DESPESA) = 'VIAGENS' GROUP BY 1 , 2) AS TMP3 ON MESES.ANOMES = TMP3.PERIODO JOIN (SELECT @VALOR_APROVADO:=0) va JOIN (SELECT @VALOR_PREVISTO:=0) vp JOIN (SELECT @VALOR_PROJETADO:=0) vr GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")

    TOT_ORC_VIG_REL_MES = PainelOrcamentosLogstash.objects.filter(grupo_despesa='VIAGENS', periodo=ano_mes_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
    TOT_ORC_VIG_REL_ANO = PainelOrcamentosLogstash.objects.filter(grupo_despesa='VIAGENS', periodo__contains=ano_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
	
# Valores Sem Classificação

    ORC_SEM_PRE_MES = ORCAMENTOS.objects.filter(despesa='Sem Classificacaco', mes=mes_corrente, ano=ano_corrente).values_list('valor', flat=True).first()
    ORC_SEM_PRE_ANO = ORCAMENTOS.objects.filter(despesa='Sem Classificacaco', ano=ano_corrente).aggregate(Sum('valor'))['valor__sum']

    ORC_SEM_REL_PER = ORCAMENTOS_PORCENTAGEM_SEM.objects.using('monitorcs').filter(tipo_despesa='NAO CLASSIFICADO').values('descricao_natureza', 'perc')
    ORC_SEM_HIST_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, grupo_despesa='NAO CLASSIFICADO').values('periodo', 'grupo_despesa').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')		
	
#    ORC_SEM_PRE_ANO_ACU = ORCAMENTOS.objects.filter(despesa='Sem Classificacao', ano=ano_corrente).values()	
    ORC_SEM_PRE_ANO_ACU = OrcamentosAcumulado.objects.raw("SELECT DISTINCT 1 AS id, ANOMES, IFNULL((VALOR_PREVISTO - VALOR_APROVADO), 0) VALOR_SALDO, IFNULL(VALOR_APROVADO, 0) VALOR_APROVADO, IFNULL(VALOR_PREVISTO, 0) VALOR_PREVISTO, IFNULL(VALOR_PROJETADO, 0) VALOR_PROJETADO FROM (SELECT  MESES.ANOMES AS ANOMES, SUM(@VALOR_APROVADO:=@VALOR_APROVADO + IFNULL(VALOR_APROVADO, 0)) VALOR_APROVADO, SUM(@VALOR_PREVISTO:=@VALOR_PREVISTO + IFNULL(VALOR_PREVISTO, 0)) AS VALOR_PREVISTO, SUM(@VALOR_PROJETADO:=@VALOR_PROJETADO + IFNULL(VALOR_PROJETADO, 0)) AS VALOR_PROJETADO FROM (SELECT CONCAT(YEAR(CURDATE()), '01') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '02') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '03') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '04') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '05') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '06') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '07') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '08') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '09') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '10') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '11') AS ANOMES UNION SELECT CONCAT(YEAR(CURDATE()), '12') AS ANOMES) AS MESES LEFT JOIN (SELECT DISTINCT TMP2.PERIODO, TMP2.DESPESA, MAX(TMP2.VALOR_APROVADO) VALOR_APROVADO, MAX(TMP2.VALOR_PREVISTO) VALOR_PREVISTO, MAX(TMP2.VALOR_PROJETADO) VALOR_PROJETADO FROM ( SELECT  ORC.PERIODO AS PERIODO, UPPER(ORC.grupo_despesa) AS DESPESA, SUM(IFNULL(ORC.valor_aprovado, 0)) AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_logstash ORC GROUP BY 1 , 2  UNION ALL  SELECT  CONCAT(ORC2.ANO, ORC2.MES) AS PERIODO, UPPER(ORC2.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, SUM(IFNULL(ORC2.valor, 0)) AS VALOR_PREVISTO, 0 AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC2 GROUP BY 1 , 2 UNION ALL SELECT  CONCAT(ORC3.ANO, ORC3.MES) AS PERIODO, UPPER(ORC3.DESPESA) AS DESPESA, 0 AS VALOR_APROVADO, 0 AS VALOR_PREVISTO, SUM(IFNULL(ORC3.valor_projetado, 0)) AS VALOR_PROJETADO FROM painel_orcamentos_orcamentos ORC3 GROUP BY 1 , 2 ) AS TMP2 WHERE UPPER(TMP2.DESPESA) = 'SEM CLASSIFICACAO' GROUP BY 1 , 2) AS TMP3 ON MESES.ANOMES = TMP3.PERIODO JOIN (SELECT @VALOR_APROVADO:=0) va JOIN (SELECT @VALOR_PREVISTO:=0) vp JOIN (SELECT @VALOR_PROJETADO:=0) vr GROUP BY ANOMES) AS RESULT ORDER BY ANOMES")

    TOT_ORC_SEM_REL_MES = PainelOrcamentosLogstash.objects.filter(grupo_despesa='NAO CLASSIFICADO', periodo=ano_mes_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']	
    TOT_ORC_SEM_REL_ANO = PainelOrcamentosLogstash.objects.filter(grupo_despesa='NAO CLASSIFICADO', periodo__contains=ano_corrente).aggregate(Sum('valor_aprovado'))['valor_aprovado__sum']		
	
	
    return render(request, 'painel_orcamentos/orcamentos.html',
        {
            'data': data,
            'ano_corrente': ano_corrente,
            'mes_corrente': mes_corrente,		
#           'Orcamentos_Previstos': Orcamentos_Previstos,

			# Benefício
            'ORC_BEN_PRE_MES': ORC_BEN_PRE_MES,
            'ORC_BEN_PRE_ANO': ORC_BEN_PRE_ANO,
            'ORC_BEN_REL_PER': ORC_BEN_REL_PER,			
            'ORC_BEN_HIST_ANO': ORC_BEN_HIST_ANO,
            'ORC_BEN_PRE_ANO_ACU': ORC_BEN_PRE_ANO_ACU,	
            'TOT_ORC_BEN_REL_MES': TOT_ORC_BEN_REL_MES,
            'TOT_ORC_BEN_REL_ANO': TOT_ORC_BEN_REL_ANO,		

			# Capacitação
            'ORC_CAP_PRE_MES': ORC_CAP_PRE_MES,
            'ORC_CAP_PRE_ANO': ORC_CAP_PRE_ANO,
            'ORC_CAP_REL_PER': ORC_CAP_REL_PER,			
            'ORC_CAP_HIST_ANO': ORC_CAP_HIST_ANO,
            'ORC_CAP_PRE_ANO_ACU': ORC_CAP_PRE_ANO_ACU,	
            'TOT_ORC_CAP_REL_MES': TOT_ORC_CAP_REL_MES,
            'TOT_ORC_CAP_REL_ANO': TOT_ORC_CAP_REL_ANO,				

			# Consumo
            'ORC_CON_PRE_MES': ORC_CON_PRE_MES,
            'ORC_CON_PRE_ANO': ORC_CON_PRE_ANO,	
            'ORC_CON_REL_PER': ORC_CON_REL_PER,			
            'ORC_CON_HIST_ANO': ORC_CON_HIST_ANO,
            'ORC_CON_PRE_ANO_ACU': ORC_CON_PRE_ANO_ACU,	
            'TOT_ORC_CON_REL_MES': TOT_ORC_CON_REL_MES,
            'TOT_ORC_CON_REL_ANO': TOT_ORC_CON_REL_ANO,				

			# Eventos
            'ORC_EVE_PRE_MES': ORC_EVE_PRE_MES,	
            'ORC_EVE_PRE_ANO': ORC_EVE_PRE_ANO,
            'ORC_EVE_REL_PER': ORC_EVE_REL_PER,			
            'ORC_EVE_HIST_ANO': ORC_EVE_HIST_ANO,
            'ORC_EVE_PRE_ANO_ACU': ORC_EVE_PRE_ANO_ACU,				
            'TOT_ORC_EVE_REL_MES': TOT_ORC_EVE_REL_MES,
            'TOT_ORC_EVE_REL_ANO': TOT_ORC_EVE_REL_ANO,			

			# Fornecedores
            'ORC_FOR_PRE_MES': ORC_FOR_PRE_MES,
            'ORC_FOR_PRE_ANO': ORC_FOR_PRE_ANO,
            'ORC_FOR_REL_PER': ORC_FOR_REL_PER,			
            'ORC_FOR_HIST_ANO': ORC_FOR_HIST_ANO,
            'ORC_FOR_PRE_ANO_ACU': ORC_FOR_PRE_ANO_ACU,
            'TOT_ORC_FOR_REL_MES': TOT_ORC_FOR_REL_MES,
            'TOT_ORC_FOR_REL_ANO': TOT_ORC_FOR_REL_ANO,	
			
			# Viagens
            'ORC_VIG_PRE_MES': ORC_VIG_PRE_MES,
            'ORC_VIG_PRE_ANO': ORC_VIG_PRE_ANO,
            'ORC_VIG_REL_PER': ORC_VIG_REL_PER,			
            'ORC_VIG_HIST_ANO': ORC_VIG_HIST_ANO,
            'ORC_VIG_PRE_ANO_ACU': ORC_VIG_PRE_ANO_ACU,
            'TOT_ORC_VIG_REL_MES': TOT_ORC_VIG_REL_MES,
            'TOT_ORC_VIG_REL_ANO': TOT_ORC_VIG_REL_ANO,

			# Sem Classificação			
            'ORC_SEM_PRE_MES': ORC_SEM_PRE_MES,
            'ORC_SEM_PRE_ANO': ORC_SEM_PRE_ANO,
            'ORC_SEM_REL_PER': ORC_SEM_REL_PER,			
            'ORC_SEM_HIST_ANO': ORC_SEM_HIST_ANO,
            'ORC_SEM_PRE_ANO_ACU': ORC_SEM_PRE_ANO_ACU,
            'TOT_ORC_SEM_REL_MES': TOT_ORC_SEM_REL_MES,
            'TOT_ORC_SEM_REL_ANO': TOT_ORC_SEM_REL_ANO,				
        })


@login_required(login_url='/login')
@permission_required('painel_orcamentos.ORCAMENTOS', raise_exception=True)
def ShowOrcamentosDetailed(request):
    import datetime
    data = datetime.datetime.now()
    d = datetime.date.today()
    ano_corrente = d.strftime('%Y')
    mes_corrente = d.strftime('%m')
    ano_mes_corrente = d.strftime('%Y%m')
	
    ORC_REL_IC_MES = PainelOrcamentosLogstash.objects.filter(periodo=ano_mes_corrente).values('periodo', 'item_contabil', 'descricao_item').annotate(valor=Sum('valor_aprovado')).order_by('periodo')
	
    ORC_REL_IC_GERAL_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente).values('periodo').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')
	
	
    return render(request, 'painel_orcamentos/orcamentos_detailed.html',
        {			
            'data': data,
            'ano_corrente': ano_corrente,
            'mes_corrente': mes_corrente,
            'ORC_REL_IC_MES': ORC_REL_IC_MES,
            'ORC_REL_IC_GERAL_ANO': ORC_REL_IC_GERAL_ANO,			
        })		
		
@login_required(login_url='/login')
def ShowOrcamentosDetailedIC(request, ic):
    import datetime
    d = datetime.date.today()
    ano_mes_corrente = d.strftime('%Y%m')

    ORC_REL_IC_DET = PainelOrcamentosLogstash.objects.filter(periodo=ano_mes_corrente, item_contabil=ic).values('periodo', 'grupo_despesa', 'item_contabil', 'descricao_natureza').annotate(tot_val=Sum('valor_aprovado')).order_by('descricao_natureza') 	

    ORC_REL_IC_DET_TOT = PainelOrcamentosLogstash.objects.filter(periodo=ano_mes_corrente, item_contabil=ic).values('periodo', 'item_contabil').annotate(valor=Sum('valor_aprovado')).order_by('periodo') 	

	
    return render(request, 'painel_orcamentos/orcamentos_detailed_model.html',
        {			
            'ORC_REL_IC_DET': ORC_REL_IC_DET,
            'ORC_REL_IC_DET_TOT': ORC_REL_IC_DET_TOT,			
        })

@login_required(login_url='/login')
@permission_required('painel_orcamentos.orcamentos')
def ShowOrcamentosDetailedICAno(request, ic):
    import datetime
    d = datetime.date.today()
    ano_corrente = d.strftime('%Y')
	
    ORC_REL_IC_DET_ANO = PainelOrcamentosLogstash.objects.filter(periodo__contains=ano_corrente, item_contabil=ic).values('periodo').annotate(tot_val=Sum('valor_aprovado')).order_by('periodo')
	
    return render(request, 'painel_orcamentos/orcamentos_detailed_ano_model.html',
        {			
            'ORC_REL_IC_DET_ANO': ORC_REL_IC_DET_ANO,		
        })			
