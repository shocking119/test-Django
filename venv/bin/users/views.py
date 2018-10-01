from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponseRedirect
from django.urls import  reverse
from django.contrib.auth.views import logout
    #Django 2.0以后不再使用：from django.contrib.auth import logout


def logout_view(request):
    #登出已登录用户
    logout(request)
    return HttpResponseRedirect(reverse('learnings:index'))