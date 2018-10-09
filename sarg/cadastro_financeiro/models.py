# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.
from clientes.models import Clientes

class ItemContabil(models.Model):
    id = models.AutoField(primary_key=True)
    cod_item_contabil = models.CharField(u'Código', max_length=5, blank = False, null = False, unique = True)
    des_item_contabil = models.CharField(u'Descrição', max_length=150, blank = False, null = False)
    TIPOS_ITEM_CONTABIL = (
        ('GNS', 'GNS'),
        ('GSR', 'GSR'),
    )
    cod_tipo_item_contabil = models.CharField(max_length=3, choices=TIPOS_ITEM_CONTABIL, blank=False, null=False)
    cliente = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.CASCADE, blank=True, null=True) 	
    def __str__(self):
        return '%s | %s' % (self.cod_item_contabil, self.des_item_contabil)

    class Meta:
        verbose_name = "Item Contabil"
        verbose_name_plural = "Itens Contabeis"


        
class Atividade(models.Model): 
    id = models.AutoField(primary_key=True)
    cod_atividade = models.CharField(u'Código', max_length=5, blank = False, null = False, unique = True)
    des_atividade = models.CharField(u'Descrição', max_length=150, blank = False, null = False)
    cod_item_contabil = models.ForeignKey(ItemContabil, verbose_name='Item Contabil', on_delete=models.CASCADE)
    def __str__(self):
        return '%s | %s' % (self.cod_atividade, self.des_atividade)

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"

