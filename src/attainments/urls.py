from django.conf.urls import url

from .views import attainment_detail


urlpatterns = [
    url(r'^attainments', attainment_detail, name='detail-view'),
]
