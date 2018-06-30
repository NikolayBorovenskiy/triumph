from django.contrib import admin

from .models import SEOVideoTotal, Video


class SEOVideoTotalModelAdmin(admin.ModelAdmin):
    list_display = ["browser_title"]

    class Meta:
        model = SEOVideoTotal


# Register your models here.
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_filter = ["date_updated", "date_created"]
    search_fields = ["title"]
    fieldsets = [
        ('SEO', {'fields': [
            'browser_title', 'h1', 'key_words', 'head_description']}),
        (u'Основные', {'fields': ['title', 'video']}),
    ]

    class Meta:
        model = Video


admin.site.register(SEOVideoTotal, SEOVideoTotalModelAdmin)
admin.site.register(Video, VideoModelAdmin)
