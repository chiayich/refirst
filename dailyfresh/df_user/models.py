# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class DfUser(models.Model):
    """用户基本信息"""
    u_name = models.CharField(max_length=30)  # 姓名
    u_password = models.CharField(max_length=40)  # 密码
    u_email = models.CharField(max_length=50)  # 邮箱
    is_del = models.BooleanField(default=False)  # 是否删除


class UserSite(models.Model):
    """用户地址类"""
    site_detail = models.CharField(max_length=50)  # 详细地址
    tel_no = models.CharField(max_length=20)  # 电话号码
    site_cid = models.CharField(max_length=15)  # 地址数字编码
    site_str = models.CharField(max_length=200)  # 地址
    site_post = models.IntegerField()  # 邮编
    user_id = models.ForeignKey('DfUser')  # 所属用户
    is_del = models.BooleanField(default=False)  # 是否删除
    set_default = models.BooleanField(default=False)  # 是否默认


class UserInfo(models.Model):
    """ 用户详细信息"""
    age = models.IntegerField(blank=True)  # 年龄
    gender = models.IntegerField(default=0)  # 性别
    birth = models.DateField(auto_now=True)  # 生日
    nike_name = models.CharField(max_length=30)
    last_sign_in = models.DateTimeField(auto_now=True)  # 最后一次登录日期
    create_date = models.DateField(auto_now_add=True)  # 创建日期
    user_id = models.OneToOneField('DfUser')  # 所属用户
    is_del = models.BooleanField(default=False)  # 是否删除
