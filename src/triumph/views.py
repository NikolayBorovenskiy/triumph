# coding: utf-8
import random

from django.shortcuts import render
from school.models import School
from galleries.models import Photo


def generate_slider_photos(photo_list, empty_photo=None):
    for photo in photo_list:
        yield photo
        if empty_photo:
            yield empty_photo


def home(request):
    school_queryset = School.objects.all()
    slider_photo_qs = Photo.objects.filter(is_slider_photo=True).order_by('?')
    # order_by('?') - randomize
    empty_photo = Photo.objects.filter(name='empty')
    slider_photos = generate_slider_photos(slider_photo_qs, empty_photo[0]) if \
        len(empty_photo) else generate_slider_photos(slider_photo_qs)
    if school_queryset:
        instance = school_queryset[0]
    else:
        instance = None
    context = {
        'instance': instance,
        'slider_photos': tuple(slider_photos),
        'title': u'Главная'
    }
    return render(request, 'home.html', context)


def robots_txt(request):
    return render(
        request, 'robots.txt', {}, content_type='text/plain')
