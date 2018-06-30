from django.shortcuts import render

from .models import SEOScheduleTotal, Schedule


def timetable_week(request):
    schedule_queryset = Schedule.objects.all()

    seo = SEOScheduleTotal.objects.first()
    context = {
        'schedules': schedule_queryset,
        'title': u'Расписание занятий',
        'browser_title': seo.browser_title,
        'h1': seo.h1,
        'keywords': seo.key_words,
        'head_description': seo.head_description,
    }

    return render(request, "time_table.html", context)
