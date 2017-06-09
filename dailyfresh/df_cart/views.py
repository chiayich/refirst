# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render, redirect

from df_cart.models import CartInfo
from df_user.user_doc import whether_login

# Create your views here.


@whether_login
def add_cart(request):
    req = request.GET
    gid = req.get('gid')
    count = req.get('count')
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(goods_id=gid).filter(user_id=uid)

    if len(carts) == 0:
        cart = CartInfo()
        cart.goods_id = int(gid)
        cart.user_id = int(uid)
        cart.count = int(count)
        cart.save()
    else:
        cart = carts[0]
        cart.count += int(count)
        cart.save()
    if request.is_ajax():
        cnt = CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({
            'cart_id': cart.id,
            'count': cnt
        })
    else:
        return redirect('/cart/list/')


@whether_login
def cart_show(request):
    req = request.GET
    uid = req.get('user_id')
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title': '购物车',
        'page_name': 1,
        'carts': carts
    }

    return render(request, 'df_cart/cart_show.html', context)


@whether_login
def edit_cart(request):
    req = request.GET
    cart_id = req.get('cart_id')
    cnt = req.get('count')
    # count = 1
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count = cart.count
        cart.count = int(cnt)
        cart.save()
        data = {
            'ok': 0
        }
    except LookupError as e:
        data = {
            'ok': count,
            'exception': e,
        }
    return JsonResponse(data)


@whether_login
def clear_cart(request):
    req = request.GET
    cart_id = req.get('cart_id')
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {
            'ok': 1
        }
    except LookupError as e:
        data ={
            'ok': 0,
            'exception': e,
        }
    return JsonResponse(data)