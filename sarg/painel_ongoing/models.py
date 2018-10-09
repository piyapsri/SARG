# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class ongoing(models.Model):
   descricao_item_contabil = models.CharField(max_length = 500)
   item_contabil = models.CharField(max_length = 5, primary_key=True, unique=True)  
   hora_normal = models.IntegerField()
   hora_75_pc = models.IntegerField()
   hora_100_pc = models.IntegerField()
   hora_total = models.IntegerField()
   periodo = models.CharField(max_length = 15)
   class Meta:
      managed = False
      db_table = 'painel_ongoing_ongoing'
