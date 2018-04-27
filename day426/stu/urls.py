from django.conf.urls import url
from stu import views

urlpatterns = [
    url(r'^stus/(\d+)/', views.show_students, name='s'),
    url(r'^redirectStu/(?P<g_id>\d+)/', views.redirectStu, name='restu'),
    # /student/stus/2018/4/1
    # url(r'allstu/(\d+)/(\d+)/(\d+)', views.selStu),
    # url(r'actstu/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.selStu),
    url(r'delstu', views.delStu),
]
