from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment

class Result(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.user

class Course(models.Model):
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.course

    # result = username.objects.all().values('username')
    # # result = User.objects.all()
    # def __str__(self):
        # return self.result
