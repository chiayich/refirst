# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


class GoodsType(models.Model):
    """商品类型"""
    title = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)
    css_class = models.CharField(max_length=20, blank=True)
    img_show = models.ImageField(upload_to='images', blank=True)

    def __unicode__(self):
        return self.title
    pass


class GoodsInfo(models.Model):
    """商品"""
    title = models.CharField(max_length=40)
    pic = models.ImageField(upload_to='goods')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_delete = models.BooleanField(default=False)
    unit = models.CharField(max_length=20, default='500g')
    click_num = models.IntegerField()
    introduce = models.CharField(max_length=200)
    inventory = models.IntegerField()
    content = HTMLField()
    goods_type = models.ForeignKey('GoodsType')

    def __unicode__(self):
        return self.title
    pass

