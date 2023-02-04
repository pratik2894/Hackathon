from django.db import models
class leavereq(models.Model):
    nameEp = models.CharField(max_length=100 , default=" ")
    email = models.TextField( max_length=100 , default=" ")
    leavereason = models.TextField()
# Create your models here.
