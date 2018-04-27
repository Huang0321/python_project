from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'^stu_fir/', views.firPage),
    url(r'stu_send/(?P<name>\w+)/(?P<sex>\w+)/(?P<birth>[\w-]+)/(?P<height>\w+)/', views.secPage, name='st'),
    url(r'stuinfo/(?P<stu_id>\d+)/', views.selStu, name='info'),
]