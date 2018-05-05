from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from nba import views

router = SimpleRouter()

router.register(r'player', views.ShowPlayers)

urlpatterns = [
    url(r'ajax/', views.AjaxPlayer)
]

urlpatterns += router.urls