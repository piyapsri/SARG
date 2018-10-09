from django.contrib import admin

# Register your models here.
from clientes.models import Clientes


class ClientesAdmin(admin.ModelAdmin):
        list_display = ('cliente', 'logo')
        list_filter = ['cliente']
        ordering = ('cliente', 'logo')
        list_per_page=10
        search_fields = ['cliente']		

admin.site.register(Clientes, ClientesAdmin)

