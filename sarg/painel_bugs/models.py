# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
	   
class FalhasEmAberto(models.Model):
   numero_ocorrencia = models.CharField(max_length = 100,unique=True,primary_key=True)
   titulo =  models.CharField(max_length = 100)
   data_criacao = models.DateField
   grupo_suporte = models.CharField(max_length = 100)
   tipo_servico = models.CharField(max_length = 100)
   class Meta:
       managed = False
       db_table = 'vw_painel_falhas_em_aberto_logstash'

class FalhasEncerradasNosUltimos6Meses(models.Model):
   numero_ocorrencia = models.CharField(max_length = 100,unique=True)
   titulo =  models.CharField(max_length = 100)
   data_criacao = models.DateField
   data_solucao = models.DateField   
   grupo_suporte = models.CharField(max_length = 100)
   tipo_servico = models.CharField(max_length = 100)
   class Meta:
       managed = False
       db_table = 'vw_painel_falhas_encerredas_nos_ultimos_6_meses_logstash'  	   
	   

	   

