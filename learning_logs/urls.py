#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""app urls"""


from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),

    # 特定主题的详细页面
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]


"""
path()
第一个参数 是匹配URL
第二个参数 指向要调用的视图函数
第三个参数 定义该URL模式的名称，让我们能够在代码的其他地方引用
"""
