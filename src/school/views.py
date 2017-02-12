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
        'title': u'О нас'
    }

    return render(request, "about_us.html", context)


def contacts_list(request):
    school_queryset = School.objects.all()
    if school_queryset:
        instance = school_queryset[0].contact
    else:
        instance = None
    context = {
        'instance': instance,
        'title': u'Контактная информация'
    }

    return render(request, "contacts.html", context)

