from django.db import models

class adminSignup(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=200 , default='' )
    phone = models.IntegerField(max_length=11)
    password = models.TextField(max_length=20)

# Create your models here.
