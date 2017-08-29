from django.shortcuts import render
from .models import Schedule, Event, Room


def timetable_week(request):
    schedule_queryset = Schedule.objects.all()
    
    context = {
        'schedules': schedule_queryset,
        'title': u'Расписание занятий'
    }
    
    return render(request, "time_table.html", context)
