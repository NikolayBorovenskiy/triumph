from django.contrib import admin

from .models import Articles, SEOArticlesTotal


class SEOArticlesTotalModelAdmin(admin.ModelAdmin):
    list_display = ["browser_title"]

    class Meta:
        model = SEOArticlesTotal


class ArticlesModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_display_links = ["date_updated"]
    list_filter = ["date_updated", "date_created"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    fieldsets = [
        ('SEO', {'fields': [
            'browser_title', 'h1', 'key_words', 'head_description']}),
        (u'Основные', {'fields': ['title', 'cover_image', 'content', ]}),
    ]

    class Meta:
        model = Articles


admin.site.register(SEOArticlesTotal, SEOArticlesTotalModelAdmin)
admin.site.register(Articles, ArticlesModelAdmin)
