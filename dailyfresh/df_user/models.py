# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DfUser(models.Model):
    u_name = models.CharField(max_length=30)
    u_password = models.CharField(max_length=40)
    u_email = models.CharField(max_length=50)
