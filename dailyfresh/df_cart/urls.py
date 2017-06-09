from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.cart_show),
    url(r'^add', views.add_cart),
    url(r'^edit', views.edit_cart),
    url(r'^delete', views.clear_cart),
]