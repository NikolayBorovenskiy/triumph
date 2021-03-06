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
        'browser_title': instance.browser_title,
        'h1': instance.h1,
        'keywords': instance.key_words,
        'head_description': instance.head_description,
    }
    return render(request, 'home.html', context)


def robots_txt(request):
    return render(
        request, 'robots.txt', {}, content_type='text/plain')


def sitemap_xml(request):
    return render(
        request, 'sitemap.xml', {}, content_type='text/plain')
