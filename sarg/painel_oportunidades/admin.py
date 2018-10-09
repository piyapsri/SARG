from django.contrib import admin

# Register your models here.

from painel_oportunidades.models import OPORTUNIDADES

class OPORTUNIDADESAdmin(admin.ModelAdmin):
	list_display = ('cliente', 'oportunidade', 'status', 'responsavel')
	list_filter = ['cliente', 'status']
#	search_fields = ('ano')
	ordering = ('cliente', 'status')
	list_per_page=10
		
admin.site.register(OPORTUNIDADES, OPORTUNIDADESAdmin)
