from django.contrib import admin

from .models import Video


# Register your models here.
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "date_updated"]
    list_filter = ["date_updated", "date_created"]
    search_fields = ["title"]
    
    class Meta:
        model = Video


admin.site.register(Video, VideoModelAdmin)
