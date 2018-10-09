# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from clientes.models import Clientes
from cadastro_financeiro.models import ItemContabil, Atividade

# Create your models here.

class PROJETOS(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.CASCADE) 
    projeto = models.CharField(u'Projeto', max_length = 150, blank=True, null=False)
    #item_contabil = models.CharField(u'Item Contábil', max_length = 150, blank=True, null=False, default='Aguardando Financeiro')
    #codigo_atividade = models.IntegerField(u'Código Atividade', blank=True, null=False, default='0')
    item_contabil = models.ForeignKey(ItemContabil, verbose_name='Item Contábil', on_delete=models.CASCADE) 
    codigo_atividade = models.ManyToManyField(Atividade, verbose_name='Cód. Atividade')#, on_delete=models.CASCADE) 
    gp = models.CharField(u'GP', max_length = 75, blank=True, null=False)
    responsavel_tecnico = models.CharField(u'Responsável Técnico', max_length = 75, blank=True, null=False)
    data_inicio = models.DateField(u'Data Inicio', default=date.today, blank=True, null=True)
    data_fim = models.DateField(u'Data Fim', default=date.today, blank=True, null=True)
    horas_previstas = models.IntegerField(u'Horas Previstas', blank=True, null=True)
    percent_conclusao = models.CharField(u'Percentual Conclusão', max_length = 4, blank=True, null=False)
    fase = models.CharField(u'Fase', max_length = 75, blank=True, null=False)
    status_choices = (
	   ('1', 'OK'),
	   ('2', 'Atenção'),
	   ('3', 'Problema'),
	   ('4', 'Pausado'),
	   ('5', 'Inativo')
    )
    #status_situacao = (
	 #  ('Ativo', 'Ativo'),
	 #  ('Inativo', 'Inativo')
	 #)
    categoria_choices = (
	   ('1', 'OnGoing'),
	   ('2', 'Projeto')
    )	
    status = models.CharField(max_length=30, choices=status_choices, blank=True, null=True)
    #situacao = models.CharField(max_length=30, choices=status_situacao, blank=True, null=True, default="Ativo")
    categoria = models.CharField(max_length=30, choices=categoria_choices, blank=True, null=True)	
    obs = models.TextField(u'Observação', blank=True, null=True)
    historico = models.TextField(u'Histórico', blank=True, null=False)


    def __str__(self):
         return '%s | %s | %s | %s' % (self.cliente, self.projeto, self.item_contabil, self.codigo_atividade)
#    class Meta:
#        unique_together = ('cliente', 'projeto')
    class Meta:
        verbose_name = "Painel de Projetos"
        verbose_name_plural = "Projetos"

class HORAS_ONGOING(models.Model):
   id = models.CharField(primary_key=True, max_length=255)  
   item_contabil = models.CharField(max_length=255)
   hora_total = models.CharField(max_length=255)
   class Meta:
      managed = False
        
