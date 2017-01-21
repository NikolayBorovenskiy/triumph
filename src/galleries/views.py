from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Gallery


def galleries_detail(request, slug=None):
    instance = get_object_or_404(Gallery, slug=slug)
    cover_photo_qs = instance.photo_set.filter(is_cover_photo=True)
    if cover_photo_qs.exists():
        cover_photo = cover_photo_qs
    else:
        cover_photo = instance.photo_set.all()
    context = {
        'title': instance.title,
        'instance': instance,
        'cover_photo': cover_photo[0]
    }
    
    return render(request, "gallery_detail.html", context)


def galleries_list(request):
    queryset_list = Gallery.objects.all()
    paginator = Paginator(queryset_list, 9)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
        'title': u'Фотогалерея'
    }
    
    return render(request, "galleries_list.html", context)
