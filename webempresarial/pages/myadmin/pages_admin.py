from django.contrib import admin
from ..mymodels.pages import Page

class PagesAdmin(admin.ModelAdmin):
    readosnly_fields = ('created', 'updated')
    list_display = ('title','order','created')

admin.site.register(Page,PagesAdmin)