# -*- coding: utf-8 -*-
from django.db import models

class DEMANDAS(models.Model):  
   tipo_servico = models.CharField(max_length = 100)
   severidade = models.CharField(max_length = 36)
   numero_ocorrencia = models.CharField(max_length = 100)
   titulo = models.CharField(max_length = 200)
   data_criacao = models.CharField(max_length = 100)
   data_solucao = models.CharField(max_length = 100)
   grupo_suporte = models.CharField(max_length = 100)
   situacao = models.CharField(max_length = 100)
   responsavel = models.CharField(max_length = 100)
   tipo = models.CharField(max_length = 100)
   servico = models.CharField(max_length = 100)
   horas_previstas = models.IntegerField()
   class Meta:
       managed = False
       db_table = 'vw_painel_demandas_logstash'