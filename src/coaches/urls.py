from django.conf.urls import url

from .views import (
    coaches_list,
)

urlpatterns = [
    url(r'^$', coaches_list, name='list'),
]
