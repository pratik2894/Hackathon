from django.db import models

class leave(models.Model):
    name = models.CharField(max_length=100 , default="")
    date1 = models.TextField(default=""),
    date2 = models.TextField(default=""),
    email = models.CharField(max_length=100 , default=" ")
    reason = models.CharField(max_length=200 , default=" ")


# Create your models here.
