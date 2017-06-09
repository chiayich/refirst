# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from df_cart.models import CartInfo
from df_order.models import OrderInfo, OrderDetailInfo
from df_user.models import DfUser
from df_user.user_doc import whether_login


@whether_login
def order(request):
    user = DfUser.objects.get(id=request.session['user_id'])
    req = request.GET
    carts_ids = req.getlist('cart_id')
    # carts_id_list = list(map(int, carts_ids))
    carts_id_list = [int(item) for item in carts_ids]
    carts = CartInfo.objects.filter(id__in=carts_id_list)
    context = {
        'title': '提交订单',
        'carts': carts,
        'user': user,
        'cart_ids': ','.join(carts_ids)
    }
    return render(request, 'df_order/order.html', context)


@whether_login
def pay(request):
    req = request.GET
    oid = req.get('oid')
    user_order = OrderInfo.objects.get(oid=oid)
    user_order.is_pay = True
    user_order.save()
    context = {
        'order': user_order
    }
    return render(request, 'df_order/pay.html', context)


@transaction.atomic()
@whether_login
def order_handle(request):
    tran_id = transaction.savepoint()
    req = request.POST
    cart_ids = req.get('cart_ids')
    try:
        user_order = OrderInfo()
        now = datetime.now()
        uid = request.session['user_id']
        user_order.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), uid)
        user_order.user_id = uid
        user_order.date = now
        user_order.address = req.get('address')
        user_order.total = 0
        user_order.save()
        cart_ids_list = [int(item) for item in cart_ids.split(',')]
        total = 0
        for idl in cart_ids_list:
            detail = OrderDetailInfo()
            detail.order = order
            cart = CartInfo.objects.get(id=idl)
            goods = cart.goods
            if goods.inventory >= cart.count:
                goods.inventory = cart.goods.inventory = cart.count
                goods.save()
                detail.goods_id = goods.id
                price = goods.price
                detail.price = price
                count = cart.count
                detail.count = count
                detail.save()
                total = total + price*count
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
            pass
        order.total = total+10
        order.save()
        transaction.savepoint_rollback(tran_id)
    except Exception as e:
        print(e)
        transaction.savepoint_rollback(tran_id)

    return redirect('/user/order/')
