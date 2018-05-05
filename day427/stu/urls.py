from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from stu import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'student', views.StudentEdit)

urlpatterns = [
    url(r'index/', login_required(views.index)),
    url(r'addstu/', views.addStu, name='add'),
    url(r'addstuinfo/(?P<stu_id>\d+)/', views.addStuInfo, name='info'),
    url(r'stupage/', views.stuPage),
    url(r'showstu/', views.showStus)
]

urlpatterns += router.urls
