from django.contrib import admin

from .models import News, SEONewsTotal


class SEONewsTotalModelAdmin(admin.ModelAdmin):
    list_display = ["browser_title"]

    class Meta:
        model = SEONewsTotal


class NewsModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_display_links = ["date_updated"]
    list_filter = ["date_updated", "date_created"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    fieldsets = [
        ('SEO', {'fields': [
            'browser_title', 'h1', 'key_words', 'head_description']}),
        (u'Основные', {'fields': ['title', 'image', 'content', ]}),
    ]

    class Meta:
        model = News


admin.site.register(SEONewsTotal, SEONewsTotalModelAdmin)
admin.site.register(News, NewsModelAdmin)
