from django.contrib import admin

from .models import Gallery, Photo


class PhotoInLine(admin.TabularInline):
    model = Photo


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_gallery']
    search_fields = ['name', 'gallery__title']
    list_filter = ['gallery__title']
    
    class Meta:
        model = Photo


class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_filter = ["date_updated", "date_created"]
    search_fields = ["title"]
    inlines = [PhotoInLine]
    
    class Meta:
        model = Gallery


admin.site.register(Gallery, GalleryModelAdmin)
admin.site.register(Photo, PhotoModelAdmin)
