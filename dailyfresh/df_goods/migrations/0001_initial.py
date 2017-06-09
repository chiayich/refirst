# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('pic', models.ImageField(upload_to='goods')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_delete', models.BooleanField(default=False)),
                ('unit', models.CharField(default='500g', max_length=20)),
                ('click_num', models.IntegerField()),
                ('introduce', models.CharField(max_length=200)),
                ('inventory', models.IntegerField()),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='goods_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsType'),
        ),
    ]
