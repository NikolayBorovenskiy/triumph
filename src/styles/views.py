from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Style, SEOStyleTotal


def styles_detail(request, slug=None):
    instance = get_object_or_404(Style, slug=slug)
    cover_photo_qs = instance.photo_set.filter(is_cover_photo=True)
    if cover_photo_qs.exists():
        cover_photo = cover_photo_qs
    else:
        cover_photo = instance.photo_set.all()

    if instance.subtitle and instance.group:
        title = "%s (%s, %s)" % (instance.title, instance.subtitle, instance.group)
    elif instance.subtitle or instance.group:
        title = "%s (%s)" % (instance.title, instance.subtitle or instance.group)
    else:
        title = instance.title

    context = {
        'title': title,
        'instance': instance,
        'cover_photo': cover_photo[0] if cover_photo else None,
        'browser_title': instance.browser_title,
        'h1': instance.h1,
        'keywords': instance.key_words,
        'head_description': instance.head_description,
    }

    return render(request, "styles_detail.html", context)


def styles_list(request):
    queryset_list = Style.objects.filter(sub_style__isnull=True)
    paginator = Paginator(queryset_list, 8)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    seo = SEOStyleTotal.objects.first()
    context = {
        'object_list': queryset,
        'browser_title': seo.browser_title,
        'h1': seo.h1,
        'keywords': seo.key_words,
        'head_description': seo.head_description,
    }

    return render(request, "styles_list.html", context)
