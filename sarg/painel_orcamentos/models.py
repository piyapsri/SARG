# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator
#from django.utils.formats import number_format

# Create your models here.

class PainelOrcamentosLogstash(models.Model):
    periodo = models.CharField(max_length=6, unique=True)
    grupo_despesa = models.CharField(max_length=255)
    cod_natureza = models.IntegerField(unique=True)
    descricao_natureza = models.CharField(max_length=30)
    centro_custo = models.CharField(max_length=5, unique=True)
    item_contabil = models.CharField(max_length=5, unique=True)
    descricao_item = models.CharField(max_length=40)
    valor_aprovado = models.DecimalField(max_digits=20, decimal_places=2)
    valor_acumulado_mes = models.DecimalField(max_digits=20, decimal_places=2)
    class Meta:
       managed = False
       db_table = 'painel_orcamentos_logstash'

class OrcamentosAcumulado(models.Model):
    ano_mes = models.CharField(max_length=6)
    valor_saldo = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    valor_aprovado = models.DecimalField(max_digits=20, decimal_places=2)
    valor_previsto = models.DecimalField(max_digits=20, decimal_places=2)

class ORCAMENTOS(models.Model):
    despesas_choices = (
	('Beneficios', 'Beneficios'),
	('Capacitacoes', 'Capacitacoes'),	
	('Consumos', 'Consumos'),	
	('Eventos', 'Eventos'),
	('Fornecedores', 'Fornecedores'),
    ('Viagens', 'Viagens'),	
	('Sem Classificacao', 'Sem Classificacao')	
    )
    despesa = models.CharField(max_length=30, choices=despesas_choices, blank=False, null=False, default='Sem Classificação')
    mes = models.CharField(max_length=2, blank=False, null=True)
    ano = models.CharField(max_length=4, blank=False, null=True)
    valor = models.DecimalField(u'Valor Previsto', max_digits=10, decimal_places=2, blank=False, null=True)
    valor_realizado = models.DecimalField(u'Valor Realizado', max_digits=10, decimal_places=2, blank=True, null=True)
    valor_projetado = models.DecimalField(u'Valor Projetado', max_digits=10, decimal_places=2, blank=True, null=True)
    def __str__(self):
         return '%s/%s - %s - R$%s - R$%s - R$%s' % (self.ano, self.mes, self.despesa, self.valor, self.valor_realizado, self.valor_projetado )
    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"
        unique_together = ('ano', 'mes', 'despesa')

	   
class ORCAMENTOS_PORCENTAGEM_BEN(models.Model):
   tipo_despesa = models.CharField(primary_key=True, max_length = 255)
   descricao_natureza = models.CharField(max_length = 255)
   valor = models.CharField(max_length = 255)
   perc = models.CharField(max_length = 255)
   valor_total = models.CharField(max_length = 255)  
   class Meta:
      managed = False
      db_table = '"PAINEL_ORCAMENTOS_PORC_BEN"' 
	  
class ORCAMENTOS_PORCENTAGEM_CAP(models.Model):
   tipo_despesa = models.CharField(primary_key=True, max_length = 255)
   descricao_natureza = models.CharField(max_length = 255)
   valor = models.CharField(max_length = 255)
   perc = models.CharField(max_length = 255)
   valor_total = models.CharField(max_length = 255)  
   class Meta:
      managed = False
      db_table = '"PAINEL_ORCAMENTOS_PORC_CAP"'

class ORCAMENTOS_PORCENTAGEM_CON(models.Model):
   tipo_despesa = models.CharField(primary_key=True, max_length = 255)
   descricao_natureza = models.CharField(max_length = 255)
   valor = models.CharField(max_length = 255)
   perc = models.CharField(max_length = 255)
   valor_total = models.CharField(max_length = 255)  
   class Meta:
      managed = False
      db_table = '"PAINEL_ORCAMENTOS_PORC_CON"' 

class ORCAMENTOS_PORCENTAGEM_EVE(models.Model):
   tipo_despesa = models.CharField(primary_key=True, max_length = 255)
   descricao_natureza = models.CharField(max_length = 255)
   valor = models.CharField(max_length = 255)
   perc = models.CharField(max_length = 255)
   valor_total = models.CharField(max_length = 255)  
   class Meta:
      managed = False
      db_table = '"PAINEL_ORCAMENTOS_PORC_EVE"'  

class ORCAMENTOS_PORCENTAGEM_FOR(models.Model):
   tipo_despesa = models.CharField(primary_key=True, max_length = 255)
   descricao_natureza = models.CharField(max_length = 255)
   valor = models.CharField(max_length = 255)
   perc = models.CharField(max_length = 255)
   valor_total = models.CharField(max_length = 255)  
   class Meta:
      managed = False
      db_table = '"PAINEL_ORCAMENTOS_PORC_FOR"' 	  
	  
class ORCAMENTOS_PORCENTAGEM_VIG(models.Model):
   tipo_despesa = models.CharField(primary_key=True, max_length = 255)
   descricao_natureza = models.CharField(max_length = 255)
   valor = models.CharField(max_length = 255)
   perc = models.CharField(max_length = 255)
   valor_total = models.CharField(max_length = 255)  
   class Meta:
      managed = False
      db_table = '"PAINEL_ORCAMENTOS_PORC_VIG"' 	  
	  
class ORCAMENTOS_PORCENTAGEM_SEM(models.Model):
   tipo_despesa = models.CharField(primary_key=True, max_length = 255)
   descricao_natureza = models.CharField(max_length = 255)
   valor = models.CharField(max_length = 255)
   perc = models.CharField(max_length = 255)
   valor_total = models.CharField(max_length = 255)  
   class Meta:
      managed = False
      db_table = '"PAINEL_ORCAMENTOS_PORC_SEM"'  	  
  
