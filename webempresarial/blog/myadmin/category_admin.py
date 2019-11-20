from django.contrib import admin
from ..models import Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','created')

admin.site.register(Category,CategoryAdmin)