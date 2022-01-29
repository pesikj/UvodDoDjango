from operator import mod
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)
    price = models.IntegerField()

class Branch(models.Model):
    city = models.CharField(max_length=50)
    founded_on = models.DateField()
    email = models.CharField(max_length=50)
    head_count = models.IntegerField()
    
