from django.db import models
from django.contrib.auth.models import User 
import datetime

class User(models.Model):
    
    def __unicode__(self):
        return " ".join([
            self.first_name,
            self.last_name,
            ])

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bodyweight= models.IntegerField()
    goals = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add = True, default = datetime.datetime.now)

    def __unicode__(self):
        return "\n".join([
            self.name,
            self.age,
            self.bodyweight,
            self.goals
            ])



