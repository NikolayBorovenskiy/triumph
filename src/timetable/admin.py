from django.contrib import admin
from .models import Schedule, Event


class ScheduleModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    filter_horizontal = ('work_days', 'rest_days',)
    
    class Meta:
        model = Schedule


class EventModelAdmin(admin.ModelAdmin):
    list_display = ["name", "get_day"]
    
    class Meta:
        model = Event


admin.site.register(Schedule, ScheduleModelAdmin)
admin.site.register(Event, EventModelAdmin)
