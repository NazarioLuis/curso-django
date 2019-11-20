from django.contrib import admin
from ..mymodels.link import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created')

admin.site.register(Link,LinkAdmin)