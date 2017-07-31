from django.conf.urls import url

from .views import timetable_week

urlpatterns = [
    url(r'^timetable$', timetable_week, name='week'),
]
