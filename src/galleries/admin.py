from django.contrib import admin

from .models import Gallery, Photo, SEOGalleryTotal


class PhotoInLine(admin.TabularInline):
    model = Photo


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_gallery']
    search_fields = ['name', 'gallery__title']
    list_filter = ['gallery__title']

    class Meta:
        model = Photo


class SEOGalleryTotalModelAdmin(admin.ModelAdmin):
    list_display = ["browser_title"]

    class Meta:
        model = SEOGalleryTotal


class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_filter = ["date_updated", "date_created"]
    search_fields = ["title"]
    inlines = [PhotoInLine]
    fieldsets = [
        ('SEO', {'fields': [
            'browser_title', 'h1', 'key_words', 'head_description']}),
        (u'Основные', {'fields': ['title']}),
    ]

    class Meta:
        model = Gallery


admin.site.register(SEOGalleryTotal, SEOGalleryTotalModelAdmin)
admin.site.register(Gallery, GalleryModelAdmin)
admin.site.register(Photo, PhotoModelAdmin)
