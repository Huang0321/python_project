# -*- coding:utf-8 -*-


from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^addstu/', views.addStu),
    url(r"selstu/", views.selectStu)
]
