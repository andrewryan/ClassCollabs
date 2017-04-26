from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your models here.


class Result(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.user

class Course(models.Model):
    course = models.CharField(max_length=20)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.course
