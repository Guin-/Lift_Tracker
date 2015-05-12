from django.db import models
from django.contrib.auth.models import User 
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bodyweight= models.IntegerField()
    goals = models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True, default = datetime.datetime.now)

    def __unicode__(self):
        return "\n".join([
            self.name,
#            self.age,
#            self.bodyweight,
            self.goals
            ])

    

