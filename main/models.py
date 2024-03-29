from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.

class Inventory(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    def __str__(self):
        return self.title + "\n" + self.description

    



class Product(models.Model):
    description = models.TextField(max_length=100)
    count = models.IntegerField()
    upc = models.IntegerField()
    manufacturer = models.TextField(max_length=100)
    inventory = models.TextField()
    price = models.IntegerField()
    total = models.IntegerField()
    def __str__(self):
        return self.description


class History(models.Model):
    title = models.TextField()
    created_at = datetime.datetime.now()
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.TextField()
    name = models.TextField()
    last = models.TextField()
    email = models.TextField()
    password = models.TextField()
    def __str__(self):
        return self.user