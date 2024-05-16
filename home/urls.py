#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/16 11:45
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home, name='home')
]