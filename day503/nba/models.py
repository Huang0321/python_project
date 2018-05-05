from django.db import models

# Create your models here.


class Player(models.Model):
    p_name = models.CharField(max_length=20)
    p_tel = models.CharField(max_length=11)
    p_height = models.CharField(max_length=10)

    class Meta:
        db_table = 'players'


class Team(models.Model):
    t_name = models.CharField(max_length=20)
    p = models.ForeignKey(Player)

    class Meta:
        db_table = 'teams'