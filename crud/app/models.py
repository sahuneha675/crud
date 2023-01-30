from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    DOB = models.DateField()
    password =  models.CharField(max_length=250)
    contact = models.CharField(max_length=10)