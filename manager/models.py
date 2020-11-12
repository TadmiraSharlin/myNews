from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Manager(models.Model):

    name = models.CharField(max_length = 50)
    utxt = models.TextField(default="")
    email = models.TextField(default="")
    ip = models.TextField(default="")
    

    def __str__(self):
        return self.name 
   