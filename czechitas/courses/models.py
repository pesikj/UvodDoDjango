from operator import mod
from django.db import models
from django.utils.translation import gettext as _

class Person(models.Model):
  first_name = models.CharField(max_length=100, verbose_name=_("first_name"))
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  active = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " (ID " + str(self.id) + ")"

    class Meta:
        verbose_name_plural = "Categories"

class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey("Branch", on_delete=models.SET_NULL, null=True, blank=True)
    lecturer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="course_lecturer")
    event_coordinator = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="courses_event_coordinator")

    def __str__(self):
        return self.name

class Branch(models.Model):
    city = models.CharField(max_length=50)
    founded_on = models.DateField()
    email = models.CharField(max_length=50)
    head_count = models.IntegerField()

    class Meta:
        verbose_name_plural = "Branches"

class Application(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    
