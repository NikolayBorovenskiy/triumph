from django.contrib import admin

from .models import Articles


class ArticlesModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_display_links = ["date_updated"]
    list_filter = ["date_updated", "date_created"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    
    class Meta:
        model = Articles


admin.site.register(Articles, ArticlesModelAdmin)
