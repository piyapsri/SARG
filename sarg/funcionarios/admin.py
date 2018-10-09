from django.contrib import admin

# Register your models here.

from funcionarios.models import Funcao, Departamento, Contrato

class FuncaoAdmin(admin.ModelAdmin):
        list_display = ('departamento', 'funcao', 'contrato', 'valor_hora' )
        list_per_page=10
        class Meta:
                verbose_name = "Função"
                verbose_name_plural = "Funções"	

admin.site.register(Funcao, FuncaoAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
        list_display = ('id', 'departamento')
        list_per_page=10

admin.site.register(Departamento, DepartamentoAdmin)

class ContratoAdmin(admin.ModelAdmin):
        list_display = ('id', 'contrato')
        list_per_page=10

admin.site.register(Contrato, ContratoAdmin)