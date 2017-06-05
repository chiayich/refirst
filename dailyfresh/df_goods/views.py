# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

from .models import GoodsInfo
from .models import GoodsType
from django.core import serializers


def index(request):

    type_list = GoodsType.objects.all()
    context = {
        'title': '首页',
        'type_list': type_list,
    }
    return render(request, 'df_goods/index.html', context)


def type_show(request):
    req = request.GET
    tid = req.tid

    pass


def list_order(request):
    req = request.GET
    type_id = req.get('tid')
    type_info = GoodsType.objects.get(pk=int(type_id))
    goods_news = type_info.goodsinfo_set.order_by('-id')[0:2]
    sort_way = req.get('sort')
    page_index = req.get('pindex')
    if sort_way == '1':
        goods_list = GoodsInfo.objects.filter(type_id=int(type_id)).order_by('-id')
    elif sort_way == '2':
        goods_list = GoodsInfo.objects.filter(type_id=int(type_id)).order_by('-price')
    elif sort_way == '3':
        goods_list = GoodsInfo.objects.filter(type_id=int(type_id)).order_by('-click_num')
    else:
        goods_list = []
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(page_index))
    context = {
        'title': type_info.title,
        'guest_cart': 1,
        'page': page,
        'typeinfo': type_info,
        'sort': sort_way,
        'news': goods_news,
        'cart_count': 0,
    }
    return render(request, 'df_goods/list_order.html', context)


def new_show(request):
    req = request.GET
    tid = req.get('tid')
    new_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('-id')[0:4]
    context = dict()
    context['result'] = 'success'
    context['message'] = serializers.serialize('json', new_list)
    json_nl = JsonResponse(context)
    return json_nl


def hot_show(request):
    req = request.GET
    tid = req.get('tid')
    new_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('-click_num')[0:4]
    context = dict()
    context['result'] = 'success'
    context['data'] = serializers.serialize('json', new_list)
    return JsonResponse(context)


def more_list(request):
    req = request.GET
    tid = req.get('tid')
    type_info = GoodsType.objects.get(pk=int(tid))
    goods_news = type_info.goodsinfo_set.order_by('-id')[0:2]
    sort_way = req.get('sort', '1')
    page_index = req.get('pindex', '1')
    if sort_way == '1':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('-id')
    elif sort_way == '2':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('-price')
    elif sort_way == '3':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('-click_num')
    else:
        goods_list = []
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(page_index))
    context = {
        'title': type_info.title,
        'guest_cart': 1,
        'page': page,
        'typeinfo': type_info,
        'sort': sort_way,
        'news': goods_news,
        'cart_count': 0,
    }
    return render(request, 'df_goods/more_list.html', context)


def detail_show(request, tid):
    goods = GoodsInfo.objects.get(pk=int(tid))
    goods.click_num += 1
    goods.save()

    news = goods.goods_type.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': goods.goods_type.title,
        'guest_cart': 1,
        'g': goods,
        'news': news,
        'id': id,
        'cart_count': 0
    }
    return render(request, 'df_goods/detail_show.html', context)
#
#
# def cart_count(request):
#     if 'user_id' in request.session:
#         return CarInfo.objects.filter(user_id=request.session['user_id']).count()
#     else:
#         return 0
