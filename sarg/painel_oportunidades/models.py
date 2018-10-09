# -*- coding: utf-8 -*-
from django.db import models
from clientes.models import Clientes
from cadastro_financeiro.models import ItemContabil, Atividade

# Create your models here.

class HORAS_OPORTUNIDADES(models.Model):
   id = models.CharField(primary_key=True, max_length=255)  
   item_contabil = models.CharField(max_length=255)
   hora_total = models.CharField(max_length=255)
   class Meta:
      managed = False
      
class OPORTUNIDADES(models.Model):
    #logo = models.ImageField(upload_to='media',  blank=True, null=False)
    #cliente = models.CharField(u'Cliente', max_length = 75, blank=True, null=False) 
    #item_contabil = models.CharField(u'Item Contbil', max_length = 150, blank=True, null=False, default='Aguardando Financeiro')
    #codigo_atividade = models.CharField(u'Código Atividade', max_length = 150, blank=True, null=False, default='Aguardando Gestor')
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.CASCADE) 
    item_contabil = models.ForeignKey(ItemContabil, verbose_name='Item Contábil', on_delete=models.CASCADE) 
    codigo_atividade = models.ManyToManyField(Atividade, verbose_name='Cód. Atividade')#, on_delete=models.CASCADE) 
    oportunidade = models.CharField(u'Oportunidade', max_length = 75, blank=True, null=False)
    status_choices = (
        ('Prospecção de novos negócios', 'Prospecção de novos negócios'),
        ('Desenvolvimento de Proposta', 'Desenvolvimento de Proposta'),
        ('Proposta Enviada', 'Proposta Enviada'),
        ('Finalizada', 'Finalizada')    
    )
    status = models.CharField(max_length=75, choices=status_choices, blank=True, null=True)
    justificativa = models.TextField(u'Justificativa Status', blank=True, null=False)
    responsavel = models.CharField(u'Responsável', max_length = 75, blank=True, null=False)
    observacao = models.TextField(u'Observação', blank=True, null=False)	
    historico = models.TextField(u'Histórico', blank=True, null=False)
    ordering = ('-created_at',) # The negative sign indicate descendent order

    def __str__(self):
         return '%s | %s' % (self.cliente, self.oportunidade)
#    def __unicode__ (self):
#        return '%s %s' %(self.cliente, self.oportunidade)
#    class Meta:
#        unique_together = ('cliente', 'oportunidade')
    class Meta:
         verbose_name = "Painel de Oportunidades"	
         verbose_name_plural = "Oportunidades"	 

