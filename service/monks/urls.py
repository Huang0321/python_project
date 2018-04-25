from django.conf.urls import url
from monks import views

urlpatterns = {
    url(r'^add_monk/', views.add_monk),
    url(r'^select_monk/', views.select_monk)
}