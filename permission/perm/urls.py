from django.conf.urls import url

from perm import views

urlpatterns = [
    url(r'^adduser/', views.addUser),
    url(r'^selperm/', views.selPerm)
]