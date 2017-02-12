from django.conf.urls import url

from .views import (
    coaches_list,
    contacts_list
)

urlpatterns = [
    url(r'^about-us$', coaches_list, name='coach-list'),
    url(r'^contacts$', contacts_list, name='contact-list'),
]
