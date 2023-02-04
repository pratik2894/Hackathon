from django.db import models

class epdata(models.Model):

    name = models.CharField(max_length=100 , default="")
    date1 = models.TextField(default=""),
    dob = models.TextField(default=""),
    email = models.CharField(max_length=100 , default=" ")
    mobile = models.IntegerField(max_length=200 , default=" ")
    gender = models.TextField(max_length=100)
    specialization =models.TextField(max_length=100 , default=" ")
    religion = models.TextField(max_length=100 , default=" ")
    Blood = models.TextField(max_length=100 , default=" ")
    role = models.TextField(max_length=100 , default=" ")
    salary = models.TextField(max_length=100 ,default=" ")
    joining = models.TextField(max_length=100 , default=" ")
    duration = models.TextField(max_length=100 , default="")

# Create your models here.
