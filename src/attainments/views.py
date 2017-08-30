from django.shortcuts import render, get_object_or_404

from .models import Attainments


def attainment_detail(request):
    qs = Attainments.objects.all()
    instance, photo_qs = None, None
    if qs:
        instance = qs[0]
        photo_qs = instance.photo_set.all()
    context = {
        'instance': instance,
        'title': u'Достижения',
        'cover_photo': photo_qs[0] if photo_qs else None
    }
    
    return render(request, "attainment_list.html", context)
