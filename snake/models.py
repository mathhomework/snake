from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Score(models.Model):
    SNAKE = 'sn'
    MEMORY = 'mg'
    GAME_CHOICES = (
        (SNAKE, 'Snake'),
        (MEMORY, 'Memory Game')
    )
    game = models.CharField(max_length=2, choices = GAME_CHOICES)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)