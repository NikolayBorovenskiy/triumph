from django.conf.urls import url

from .views import (
    coaches_list,
    contacts_list
)

urlpatterns = [
    url(r'^about-us$', coaches_list, name='coaches'),
    url(r'^contacts$', contacts_list, name='contacts'),
]
