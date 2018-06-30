from django.contrib import admin

from .models import Event, Room, SEOScheduleTotal, Schedule


class SEOScheduleTotalModelAdmin(admin.ModelAdmin):
    list_display = ["browser_title"]

    class Meta:
        model = SEOScheduleTotal


class EventInLine(admin.TabularInline):
    model = Event


class ScheduleModelAdmin(admin.ModelAdmin):
    list_display = ["title", "room"]
    filter_horizontal = ('work_days', 'rest_days',)
    inlines = [EventInLine]

    class Meta:
        model = Schedule


class EventModelAdmin(admin.ModelAdmin):
    list_display = ["name", "get_day"]

    class Meta:
        model = Event


class RoomModelAdmin(admin.ModelAdmin):
    list_display = ["name", "number"]

    class Meta:
        model = Room


admin.site.register(SEOScheduleTotal, SEOScheduleTotalModelAdmin)
admin.site.register(Schedule, ScheduleModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(Room, RoomModelAdmin)
