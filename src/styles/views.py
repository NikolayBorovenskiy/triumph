from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Style


def styles_detail(request, slug=None):
    instance = get_object_or_404(Style, slug=slug)
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

    return render(request, "styles_detail.html", context)


def styles_list(request):
    queryset_list = Style.objects.order_by('id')
    paginator = Paginator(queryset_list, 8)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
        'title': u'Направления танца'
    }

    return render(request, "styles_list.html", context)
