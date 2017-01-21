from django.conf.urls import url

from .views import (
    articles_list,
    articles_detail,
)

urlpatterns = [
    url(r'^$', articles_list, name='list'),
    url(r'^(?P<slug>[\w-]+)$', articles_detail, name='detail'),
]
