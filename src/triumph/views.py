# coding: utf-8

from django.shortcuts import render
from school.models import School


def home(request):
    school_queryset = School.objects.all()
    if school_queryset:
        instance = school_queryset[0]
    else:
        instance = None
    context = {
        'instance': instance,
        'title': u'Главная'
    }
    return render(request, 'home.html', context)


def robots_txt(request):
    return render(
        request, 'robots.txt', {}, content_type='text/plain')
