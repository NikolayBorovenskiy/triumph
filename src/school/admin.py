from django.contrib import admin
from .models import *


class PhotoInLine(admin.TabularInline):
    model = Photo


class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines = [PhotoInLine]
    
    class Meta:
        model = School


class CoachModelAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name"]
    search_fields = ["last_name", "first_name"]
    
    class Meta:
        model = Coach


class DanceHallPhotoInLine(admin.TabularInline):
    model = Image


class DanceHallModelAdmin(admin.ModelAdmin):
    list_display = ["id", "get_school"]
    search_fields = ["description"]
    inlines = [DanceHallPhotoInLine]
    
    class Meta:
        model = DanceHall


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["address", "phones"]
    
    class Meta:
        model = Contact

admin.site.register(School, SchoolModelAdmin)
admin.site.register(Coach, CoachModelAdmin)
admin.site.register(DanceHall, DanceHallModelAdmin)
admin.site.register(Contact, ContactModelAdmin)
