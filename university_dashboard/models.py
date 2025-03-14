from tkinter.constants import CASCADE

from django.db import models
from django.db.models import SET_NULL


# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    kafedra = models.ForeignKey(Kafedra, null=True, on_delete=SET_NULL)
    subject = models.ForeignKey(Subject, null=True, on_delete=SET_NULL)



class Group(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    group = models.ForeignKey(Group, null=True, on_delete=SET_NULL)
    image = models.ImageField(upload_to='images', null=True)


