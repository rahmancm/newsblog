from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class user(models.Model):
    user = models.CharField(User, max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user


class news(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.title
