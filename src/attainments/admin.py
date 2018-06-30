from django.contrib import admin

from .models import (Attainments, Diploma, Photo)


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = Photo


class DiplomaModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = Diploma


class PhotoInLine(admin.TabularInline):
    model = Photo


class DiplomaInLine(admin.TabularInline):
    model = Diploma


class AchievementModelAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    inlines = [PhotoInLine, DiplomaInLine]
    fieldsets = [
        ('SEO', {'fields': [
            'browser_title', 'h1', 'key_words', 'head_description']}),
        (u'Основные', {'fields': ['intro', 'content', ]}),
    ]

    class Meta:
        model = Attainments


admin.site.register(Attainments, AchievementModelAdmin)
