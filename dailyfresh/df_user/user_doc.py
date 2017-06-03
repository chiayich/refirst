# -*- coding:utf-8 -*-
# from django.shortcuts import  redirect
from django.http import HttpResponseRedirect


def whether_login(func):
    def login_fun(request, *args, **kwargs):
        if 'user_id' in request.sessions:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun
