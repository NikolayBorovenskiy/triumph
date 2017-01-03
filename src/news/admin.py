from django.contrib import admin

from .models import News


class NewsModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_display_links = ["date_updated"]
    list_filter = ["date_updated", "date_created"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    
    class Meta:
        model = News


admin.site.register(News, NewsModelAdmin)
