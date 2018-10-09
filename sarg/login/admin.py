from django.contrib import admin

# Register your models here.

from login.models import homeImagens

class HomeImagensAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'sub_titulo', 'imagem', 'status')
	list_filter = ['titulo', 'sub_titulo', 'imagem', 'status']
	list_per_page=7
		

admin.site.register(homeImagens, HomeImagensAdmin)
