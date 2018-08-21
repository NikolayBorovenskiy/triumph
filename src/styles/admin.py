from django.contrib import admin

from .models import Photo, SEOStyleTotal, Style


class SEOStyleTotalModelAdmin(admin.ModelAdmin):
    list_display = ["browser_title"]

    class Meta:
        model = SEOStyleTotal


class PhotoInLine(admin.TabularInline):
    model = Photo


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_style']
    search_fields = ['name', 'style__title']
    list_filter = ['style__title']

    class Meta:
        model = Photo


class StyleModelAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "group"]
    search_fields = ["title"]
    inlines = [PhotoInLine]
    fieldsets = [
        ('SEO', {'fields': [
            'browser_title', 'h1', 'key_words', 'head_description']}),
        (u'Основные', {'fields': ['title', 'subtitle', 'group', 'content']}),
    ]

    class Meta:
        model = Style


admin.site.register(SEOStyleTotal, SEOStyleTotalModelAdmin)
admin.site.register(Style, StyleModelAdmin)
admin.site.register(Photo, PhotoModelAdmin)
