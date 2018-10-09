from django.contrib import admin

 #Register your models here.

from painel_gmuds.models import GMUDS

class GMUDSAdmin(admin.ModelAdmin):
   list_display = ('titulo', 'status', 'data', 'cliente', 'servico', 'responsavel')
   list_filter = ['status', 'cliente', 'data', 'servico']
#	search_fields = ('ano')
   ordering = ('status', 'data')
   list_per_page=10
		
admin.site.register(GMUDS, GMUDSAdmin)