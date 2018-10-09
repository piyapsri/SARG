# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class ResumoRateioHorasGns(models.Model):  
   id_tipo = models.CharField(max_length = 100,unique=True,primary_key=True)
   id_atividade = models.IntegerField()
   descricao = models.CharField(max_length = 100)
   des_item_contabil = models.CharField(max_length = 100)
   id_ic = models.CharField(max_length = 10)
   descricao_ic = models.CharField(max_length = 100)
   periodo = models.CharField(max_length = 15)
   qtd_horas = models.FloatField()   
   class Meta:
       managed = False
       db_table = 'painel_rateio_horas_por_ic_ativ_logstash'
