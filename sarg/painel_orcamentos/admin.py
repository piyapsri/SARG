from django.contrib import admin

# Register your models here.

from painel_orcamentos.models import ORCAMENTOS

#class ORCAMENTOSAdmin(admin.ModelAdmin):
#    def queryset(self, request):
#        qs = super(ORCAMENTOSAdmin, self).queryset(request)
#        return qs.order_by('ano')
class ORCAMENTOSAdmin(admin.ModelAdmin):
	list_display = ('ano', 'mes', 'despesa', 'valor', 'valor_realizado', 'valor_projetado')
	list_filter = ['ano', 'mes', 'despesa', 'valor']
#	readonly_fields = ('ano', 'mes', 'despesa')
#	search_fields = ('ano')
#	ordering = ('ano', 'mes')
	list_per_page=12
		

admin.site.register(ORCAMENTOS, ORCAMENTOSAdmin)


