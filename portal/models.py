from django.db import models
from django.contrib.auth.models import User 

class User(models.Model):
    
    def __unicode__(self):
        return " ".join([
            self.first_name,
            self.last_name,
            ])
