# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0004_auto_20170601_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(default=0),
        ),
    ]
