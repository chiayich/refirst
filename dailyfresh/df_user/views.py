# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from hashlib import sha1

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect

from df_goods.models import GoodsInfo
from df_order.models import OrderInfo
from user_doc import whether_login
# Create your views here.
from .models import DfUser, UserInfo, UserSite
from django.core.exceptions import ObjectDoesNotExist


def login(request):
    user_name = request.COOKIES.get('user_name', '')
    context = {'title': '用户登录',
               'error_name': 0,
               'error_password': 0,
               'user_name': user_name}

    return render(request, 'df_user/login.html', context)


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


@whether_login
def site_list(request):
    uid = request.session['user_id']
    # user = UserInfo.objects.get(id=uid)
    site_list = UserSite.objects.get(user_id=uid)
    return None


def info(request):
    uid = request.session['user_id']

    try:
        exist_user_info = UserInfo.objects.get(user_id=uid)
    except ObjectDoesNotExist:
        user_info = UserInfo()
        user_info.user_id_id = uid
        user_info.save()
    else:
        user_info = exist_user_info

    user = DfUser.objects.get(id=uid)

    goods_list = []
    goods_ids = request.COOKIES.get('scan_his', '')
    if goods_ids:
        goods_ids_param = goods_ids.split(',')
        for gid in goods_ids_param:
            goods_list.append(GoodsInfo.objects.get(id=int(gid)))

    context = {
        'title': '用户中心',
        'user_name': user.u_name,
        'user_email': user.u_email,
        'user_birth': user_info.birth,
        'goods_list': goods_list,
    }
    return render(request, 'df_user/user_center_info.html', context)


@whether_login
def order(request):
    req = request.GET
    pindex = req.get('pindex')
    user_id = request.session.get('user_id')
    order_list = OrderInfo.objects.filter(user_id=user_id)
    paginator = Paginator(order_list, 2)
    if pindex == '':
        pindex = '1'
    page = paginator.page(int(pindex))

    context = {
        'title': '用户中心',
        'page_name': 1,
        'paginator': paginator,
        'page': page,
    }

    return render(request, 'df_user/user_center_order.html', context)


def logout(request):
    request.session.flush()
    return redirect('/')


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    context = {
        'count': count
    }
    return JsonResponse(context)
