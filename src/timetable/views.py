from django.shortcuts import render
from .models import Schedule, Event


def timetable_week(request):
    schedule_queryset = Schedule.objects.all()
    if schedule_queryset:
        timetable = schedule_queryset[0]
        days = list(map(lambda day: day.title, timetable.work_days.all()))
    else:
        timetable = None
        days = None
    
    context = {
        'timetable': timetable,
        'days': ",".join(days),
        'events': Event.objects.all(),
        'title': u'Расписание занятий'
    }
    return render(request, "time_table.html", context)
