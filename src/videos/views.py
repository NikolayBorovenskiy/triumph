from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Video


@xframe_options_exempt
def videos_detail(request, slug=None):
    instance = get_object_or_404(Video, slug=slug)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, "video_detail.html", context)


def videos_list(request):
    queryset_list = Video.objects.all()
    paginator = Paginator(queryset_list, 9)
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
        'title': u'Видео'
    }
    
    return render(request, "videos_list.html", context)
