# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from hashlib import sha1

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from df_user.models import DfUser


def login(request):
    user_name = request.COOKIES.get('user_name', '')
    context = {'title': '用户登录',
               'error_name': 0,
               'error_password': 0,
               'user_name': user_name}

    return render(request, 'df_user/login.html', context)


def index(request):
    context = {
        'title': '首页',
    }
    return render(request, 'index.html', context)


def register(request):

    return render(request, 'df_user/register.html')


def login_handle(request):
    req = request.POST
    user_name = req.get('user_name')
    user_password = req.get('user_password')
    keep_name = req.get('keep_name')
    users = DfUser.objects.filter(u_name=user_name)  # []
    if len(users) == 1:
        s1 = sha1()
        s1.update(user_password)
        if s1.hexdigest() == users[0].u_password:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            # xxxx
            red.set_cookie('url', '', max_age=-1)
            if keep_name != 0:
                red.set_cookie('user_name', user_name)
            else:
                red.set_cookie('user_name', '', max_age=-1)
            # xxxx
            request.session['user_id'] = users[0].id
            request.session['user_name'] = user_name
            return red
        else:
            context = {
                'title': '用户登录',
                'error_name': 0,
                'error_password': 1,
                'user_name': user_name
            }
            return render(request, 'df_user/login.html', context)
    else:
        context = {
            'title': '用户登录',
            'error_name': 1,
            'error_password': 0,
            'user_name': user_name,
            'user_password': user_password
        }
        return render(request, 'df_user/login.html', context)


def register_handle(request):
    req = request.POST
    user_name = req.get('user_name')
    user_password = req.get('pwd')
    c_password = req.get('c_pwd')
    user_email = req.get('email')
    if user_password != c_password:
        print('123')
        return redirect('/user/register/')
    s1 = sha1()
    s1.update(user_password)
    password = s1.hexdigest()
    user = DfUser()
    user.u_name = user_name
    user.u_password = password
    user.u_email = user_email
    user.save()
    return redirect('/user/login/')


def site_list(request):

    return None


def info(request):
    user = DfUser.objects.get(id=request.session['user_id'])
    user_info = user.userinfo

    context = {
        'title': '用户中心',
        'user_name': user.u_name,
        'user_email': user.u_email,
        'user_birth': user.userinfo.birth,
        'goods_list': [],
    }
    return render(request, 'df_user/user_center_info.html', context)


def order(request):
    req = request.GET
    user_id = req.get('user_id')
    return None


def logout(request):
    request.session.flush()
    return redirect('/')
