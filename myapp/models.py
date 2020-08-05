from django.db import models

# Create your models here.
from django.contrib import admin

# Register your models here.

class vehicle(models.Model):
 name = models.CharField(max_length=120)
 price = models.IntegerField()