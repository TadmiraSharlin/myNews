from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):

    name = models.CharField(max_length = 50)
    about = models.TextField()
    about_txt = models.TextField(default="")

    fb = models.CharField(max_length = 100)
    tw = models.CharField(max_length = 100)
    yt = models.CharField(max_length = 100)   
    tell = models.CharField(max_length = 100, default="-")
    link = models.CharField(max_length = 100, default="-")

    set_name = models.CharField(max_length = 50)

    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")

    def __str__(self):
        return self.set_name + " | " + str(self.pk)
   