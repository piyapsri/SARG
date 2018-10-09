# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from clientes.models import Clientes

# Create your models here.
class GMUDS(models.Model):
   #logo = models.ImageField(upload_to='media', blank=True, null=False)
   #cliente = models.CharField(u'Cliente', max_length = 75, blank=True, null=False) 
   id = models.AutoField(primary_key=True)
   cliente = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.CASCADE) 
   data = models.DateField(u'Data', default=date.today, blank=True, null=True)
   servico = models.CharField(u'Serviço', max_length = 75, blank=True, null=False)   
   responsavel = models.CharField(u'Responsável', max_length = 75, blank=True, null=False)   
   titulo = models.CharField(u'Título', max_length = 75, blank=True, null=False)
   status_choices = (
      ('Ativa', 'Ativa'),
      ('Inativa', 'Inativa')    
   )
   status = models.CharField(max_length=75, choices=status_choices, blank=True, null=True)   
   def __str__(self):
      return '%s | %s' % (self.cliente, self.titulo)
   class Meta:
      verbose_name = "Painel de GMUDs"	   
      verbose_name_plural = "GMUDs"	   
