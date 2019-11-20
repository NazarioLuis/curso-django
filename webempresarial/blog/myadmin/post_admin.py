from django.contrib import admin
from ..models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','post_categories','published')
    search_fields = ('title','author__username')
    date_hierarchy = ('published')
    list_filter = ('author__username','categories__name')

    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all()])

    post_categories.short_description = "Categorías"

admin.site.register(Post,PostAdmin)