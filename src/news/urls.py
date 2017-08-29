from django.conf.urls import url

from .views import (
    news_list,
    news_detail,
)

urlpatterns = [
    url(r'^$', news_list, name='the-news'),
    url(r'^(?P<slug>[\w-]+)$', news_detail, name='detail'),
]
