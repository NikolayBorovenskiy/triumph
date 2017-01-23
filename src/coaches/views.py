from django.shortcuts import render
from .models import Coach


def coaches_list(request):
    queryset = Coach.objects.all()

    context = {
        'object_list': queryset,
        'title': u'Наши тренеры'
    }

    return render(request, "coaches_list.html", context)
