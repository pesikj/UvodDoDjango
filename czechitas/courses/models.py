from operator import mod
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " (ID " + str(self.id) + ")"

class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="X")

class Branch(models.Model):
    city = models.CharField(max_length=50)
    founded_on = models.DateField()
    email = models.CharField(max_length=50)
    head_count = models.IntegerField()
    
