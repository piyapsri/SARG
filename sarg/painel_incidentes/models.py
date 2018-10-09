# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class OcorrenciasEmAberto(models.Model):
   numero_ocorrencia = models.CharField(max_length = 100, unique=True, primary_key=True)
   titulo =  models.CharField(max_length = 200)
   data_criacao = models.DateField()
   grupo_suporte = models.CharField(max_length = 100)
   tipo_servico = models.CharField(max_length = 100)
   situacao = models.CharField(max_length = 100)   
   class Meta:
       managed = False
       db_table = 'vw_painel_ocorrencias_em_aberto_logstash'

class OcorrenciasEmAbertoGraph(models.Model):
   servico = models.CharField(max_length = 100, primary_key=True)
   aguardando =  models.DecimalField(max_digits=10, decimal_places=2)
   atendimento = models.DecimalField(max_digits=10, decimal_places=2)
   encaminhado = models.DecimalField(max_digits=10, decimal_places=2)
   total = models.DecimalField(max_digits=10, decimal_places=2)
   class Meta:
       managed = False
       db_table = 'vw_painel_ocorrencias_em_aberto_graph'  
	     
	   
class OcorrenciasAbertasNoMes(models.Model):
   numero_ocorrencia = models.CharField(max_length = 100,unique=True)
   titulo =  models.CharField(max_length = 200)
   data_criacao = models.DateField
   data_solucao = models.DateField   
   grupo_suporte = models.CharField(max_length = 100)
   tipo_servico = models.CharField(max_length = 100)
   class Meta:
       managed = False
       db_table = 'vw_painel_ocorrencias_abertas_no_mes_logstash' 
	   
class OcorrenciasEncerradasMesAtual(models.Model):
   numero_ocorrencia = models.CharField(max_length = 100,unique=True,primary_key=True)
   titulo =  models.CharField(max_length = 200)
   data_criacao = models.DateField
   data_solucao = models.DateField   
   grupo_suporte = models.CharField(max_length = 100)
   tipo_servico = models.CharField(max_length = 100)
   class Meta:
       managed = False
       db_table = 'vw_painel_ocorrencias_encerradas_no_mes_atual_logstash' 	   
