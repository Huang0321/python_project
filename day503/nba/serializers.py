
from rest_framework import serializers

from nba.models import Player


class PlayerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'p_name', 'p_tel', 'p_height']

    def to_representation(self, instance):

        data = super().to_representation(instance)
        print(type(instance))
        # try:
        data['team'] = instance.team_set.get().t_name
        # except Exception as e:
        #     data['team'] = ''

        return data