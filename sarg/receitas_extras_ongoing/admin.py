from django.contrib import admin
from django.db import models

# Register your models here.
from receitas_extras_ongoing.models import ReceitasExtrasOngoing



class ReceitasExtrasOngoingAdmin(admin.ModelAdmin):
	list_display = ('data', 'cliente', 'tipo_atividade', 'identificador_atividade', 'valor_orcado')
	search_fields = ['data', 'tipo_atividade', 'identificador_atividade', 'valor_orcado', 'item_contabil__cod_item_contabil', 'cliente__logo']
#	raw_id_fields  = ('item_contabil',)
	autocomplete_fields = ['item_contabil', 'cliente']


admin.site.register(ReceitasExtrasOngoing, ReceitasExtrasOngoingAdmin)
