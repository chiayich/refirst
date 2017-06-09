# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from df_goods.models import GoodsInfo
from df_user.models import UserInfo, DfUser


class CartInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    user = models.ForeignKey(DfUser)

    pass
