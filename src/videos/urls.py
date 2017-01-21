from django.conf.urls import url

from .views import (
    videos_list,
    videos_detail,
)

urlpatterns = [
    url(r'^$', videos_list, name='list'),
    url(r'^(?P<slug>[\w-]+)$', videos_detail, name='detail'),
]
