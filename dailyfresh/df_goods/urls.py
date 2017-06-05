from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_show', views.new_show),
    url(r'^hot_show', views.hot_show),
    url(r'^more_list', views.more_list),
    url(r'^(\d+)/$', views.detail_show),
]
