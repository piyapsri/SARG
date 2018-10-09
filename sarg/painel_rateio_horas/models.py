# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class RateioHoras(models.Model):  
   id_func = models.CharField(max_length = 100,unique=True,primary_key=True)
   nome = models.CharField(max_length = 100)
   semana_1 = models.CharField(max_length = 13)
   semana_2 = models.CharField(max_length = 13)
   semana_3 = models.CharField(max_length = 13)
   semana_4 = models.CharField(max_length = 13)
   semana_5 = models.CharField(max_length = 13)
   periodo = models.CharField(max_length = 100)
   estatus = models.CharField(max_length = 10)
   ultima_semana_periodo = models.IntegerField()
   class Meta:
       managed = False
       db_table = 'painel_rateio_horas_por_pessoa_logstash'
       
