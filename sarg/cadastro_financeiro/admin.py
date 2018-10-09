from django.contrib import admin

# Register your models here.
from cadastro_financeiro.models import ItemContabil, Atividade


class ItemContabilAdmin(admin.ModelAdmin):
        list_display = ('cod_item_contabil', 'des_item_contabil')
        list_filter = ['cod_item_contabil', 'des_item_contabil']
        ordering = ('cod_item_contabil', 'des_item_contabil')
        list_per_page=10
        search_fields = ['des_item_contabil']


admin.site.register(ItemContabil, ItemContabilAdmin)


class AtividadeAdmin(admin.ModelAdmin):
        list_display = ('cod_atividade', 'des_atividade')
        list_filter = ['cod_atividade', 'des_atividade']
        ordering = ('cod_atividade', 'des_atividade')
        list_per_page=10

admin.site.register(Atividade, AtividadeAdmin)

