from django.contrib import admin
from .models import SEO

# Register your models here.
class SEOModelAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = SEO

admin.site.register(SEO, SEOModelAdmin)