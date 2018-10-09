# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from cadastro_financeiro.models import ItemContabil
from clientes.models import Clientes

# Create your models here.
class ReceitasExtrasOngoing(models.Model):
	id = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE) 
	item_contabil = models.ForeignKey(ItemContabil, on_delete=models.CASCADE)
	escolhas_tipo_atividade = (
	('ARS', 'ARS'),
	('PRJ', 'PRJ'),	
	('STI', 'STI'),
	('Outros', 'Outros'),	
	('Change Request', 'Change Request')
	)
	tipo_atividade = models.CharField(u'Tipo Atividade', max_length=75, choices=escolhas_tipo_atividade, )
	identificador_atividade = models.CharField(u'Identificador Atividade', max_length=75)
	data = models.DateField(u'Data', default=date.today, )
	valor_orcado = models.DecimalField(u'Valor Orçado', max_digits=20, 
	decimal_places=2)
	horas_orcadas = models.DecimalField(u'Horas Orçadas', max_digits=12, 
	decimal_places=2)
	previsao_faturamento = models.TextField(u'Previsão Faturamento', blank=True, null=True)
	impacto_ongoing = models.TextField(u'Impacto Ongoing', blank=True, null=True)
	implementado = models.TextField(u'Implementado', blank=True, null=True)
	data_implatacao = models.DateField(u'Data Implantação', blank=True, null=True)

class receitas_extras_ongoing_operadoras(models.Model):
	ano_mes = models.IntegerField()
	valor_total = models.DecimalField(decimal_places=2, max_digits=10)
	cliente = models.CharField(max_length=255, primary_key=True)
	class Meta:
		managed = False
		db_table = 'receitas_extras_ongoing_operadoras'

	

		

	

