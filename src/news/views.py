from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News, SEONewsTotal


def news_detail(request, slug=None):
    instance = get_object_or_404(News, slug=slug)
    context = {
        'title': instance.title,
        'instance': instance,
        'browser_title': instance.browser_title,
        'h1': instance.h1,
        'keywords': instance.key_words,
        'head_description': instance.head_description,
    }

    return render(request, "news_detail.html", context)


def news_list(request):
    queryset_list = News.objects.all()
    paginator = Paginator(queryset_list, 6)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    seo = SEONewsTotal.objects.first()
    context = {
        'object_list': queryset,
        'browser_title': seo.browser_title,
        'h1': seo.h1,
        'keywords': seo.key_words,
        'head_description': seo.head_description,
    }

    return render(request, "news_list.html", context)
