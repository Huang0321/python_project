from django.shortcuts import render
from rest_framework import mixins, viewsets
from nba.models import Player
from nba.serializers import PlayerSerializers
# Create your views here.


class ShowPlayers(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = Player.objects.all()

    serializer_class = PlayerSerializers


def AjaxPlayer(request):

    if request.method == 'GET':

        return render(request, 'player_info.html')