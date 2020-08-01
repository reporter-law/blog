"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),

]