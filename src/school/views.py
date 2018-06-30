from django.shortcuts import render
from .models import School


def coaches_list(request):
    school_queryset = School.objects.all()
    if school_queryset:
        instance = school_queryset[0]
    else:
        instance = None
    context = {
        'instance': instance,
        'browser_title': instance.browser_title,
        'h1': instance.h1,
        'keywords': instance.key_words,
        'head_description': instance.head_description,
    }

    return render(request, "about_us.html", context)


def contacts_list(request):
    school_queryset = School.objects.all()
    if school_queryset:
        instance = school_queryset[0]

    else:
        instance = None
    context = {
        'instance': instance.contact,
        'browser_title': instance.browser_title,
        'h1': instance.h1,
        'keywords': instance.key_words,
        'head_description': instance.head_description,
    }

    return render(request, "contacts.html", context)

