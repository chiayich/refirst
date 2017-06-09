# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from df_goods.models import GoodsInfo
from df_user.models import DfUser, UserSite


class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey(DfUser)
    date = models.DateTimeField(auto_now_add=True)
    is_pay = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.ForeignKey(UserSite)

# 无法实现：　真实支付，　物流信息


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    count = models.IntegerField()
