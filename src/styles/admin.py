from django.contrib import admin

from .models import Style, Photo


class PhotoInLine(admin.TabularInline):
    model = Photo


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_style']
    search_fields = ['name', 'style__title']
    list_filter = ['style__title']
    
    class Meta:
        model = Photo


class StyleModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    inlines = [PhotoInLine]
    
    class Meta:
        model = Style


admin.site.register(Style, StyleModelAdmin)
admin.site.register(Photo, PhotoModelAdmin)
