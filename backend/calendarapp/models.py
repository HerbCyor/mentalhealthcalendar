from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Day(models.Model):

    class Color(models.IntegerChoices):
        BLACK = 0
        RED = 1
        ORANGE = 2
        YELLOW = 3
        GREEN = 4
        BLUE = 5

    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    date = models.DateField()
    mood_score = models.IntegerField(choices=Color.choices)
    comments = models.TextField(null=True, blank=True)
