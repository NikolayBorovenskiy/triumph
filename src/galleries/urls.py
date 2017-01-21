from django.conf.urls import url

from .views import (
    galleries_list,
    galleries_detail,
)

urlpatterns = [
    url(r'^$', galleries_list, name='list'),
    url(r'^(?P<slug>[\w-]+)$', galleries_detail, name='detail'),
]
