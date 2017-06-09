# coding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),  # 跳转登陆页面
    url(r'^login_handle/$', views.login_handle),  # 登陆校验
    url(r'^logout/$', views.logout),  # 退出登陆

    url(r'^register/$', views.register),  # 跳转注册页面
    url(r'^register_handle/$', views.register_handle),  # 提交注册
    url(r'^register_exist/', views.register_exist),  # 用户是否存在

    url(r'^info/$', views.info),  # 用户信息
    url(r'^order/$', views.order),  # 订单
    url(r'^site_list/', views.site_list),  # 地址
]
