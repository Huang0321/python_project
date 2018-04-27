from django.conf.urls import url
from stu import views


urlpatterns = [
    url(r"^addstu", views.addStu),
    url(r"^selstu", views.selStu),
    url(r"^fselstu", views.fselStu),
    url(r"^manygoods", views.manyGoods),
    url(r"^stu/", views.allStu),
    url(r'^delstu', views.delStu)
]

