from django.contrib import admin

# Register your models here.

from painel_projetos.models import PROJETOS

class PROJETOSAdmin(admin.ModelAdmin):
	list_display = ('projeto', 'cliente', 'gp', 'responsavel_tecnico', 'percent_conclusao', 'status')
	list_filter = ['status', 'cliente', 'gp']
#	search_fields = ('ano')
	ordering = ('cliente', 'status')
	list_per_page=10
		
admin.site.register(PROJETOS, PROJETOSAdmin)

