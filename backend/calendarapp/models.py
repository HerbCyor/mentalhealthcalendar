from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Calendar(models.Model):
    name = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_calendar(sender,instance,created,**kwargs):
        if created:
            Calendar.objects.create(user=instance,name=instance.username)
    
    @receiver(post_save, sender=User)
    def save_calendar(sender,instance,**kwargs):
        instance.calendar.save()

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
