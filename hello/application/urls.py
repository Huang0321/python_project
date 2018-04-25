# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from application import views


urlpatterns = [
    url(r'show', views.show),
    url(r'add', views.addStudent)
]
