
# -*- coding:utf-8 -*-
from django.conf.urls import url
from firstapp import views


urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^show/', views.show)
]
