from django.contrib import admin
from .models import Coach


class CoachModelAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name"]
    search_fields = ["last_name", "first_name"]
    
    class Meta:
        model = Coach


admin.site.register(Coach, CoachModelAdmin)
