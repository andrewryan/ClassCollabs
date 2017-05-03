from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings


class Course(models.Model):
    course = models.CharField(max_length=20)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.course

# Model used to keep a record of currently logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user')
