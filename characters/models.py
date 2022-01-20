from django.db import models


class Hero(models.Model):
    nickname = models.CharField(max_length=30)
    hero_points = models.IntegerField()
    strength = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    hp = models.IntegerField()
    xp = models.IntegerField()
    lvl = models.PositiveSmallIntegerField()


class Monster(models.Model):
    name = models.CharField(max_length=40)
    strength = models.IntegerField()
    speed = models.PositiveSmallIntegerField()
    hp = models.IntegerField()
    xp_if_win = models.IntegerField()
    lvl = models.PositiveSmallIntegerField()


class NPC(models.Model):
    name = models.CharField(max_length=30)
    has_quest = models.BooleanField()
    xp_if_completed = models.IntegerField(default=0)
