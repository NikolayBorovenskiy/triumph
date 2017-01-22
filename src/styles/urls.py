from django.conf.urls import url

from .views import (
    styles_list,
    styles_detail,
)

urlpatterns = [
    url(r'^$', styles_list, name='list'),
    url(r'^(?P<slug>[\w-]+)$', styles_detail, name='detail'),
]
