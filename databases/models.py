# -*- coding: utf-8 -*-


from django.db import models
from websiteFunctions.models import Websites

# Create your models here.

class Databases(models.Model):
    website = models.ForeignKey(Websites, on_delete=models.CASCADE)
    dbName = models.CharField(max_length=50,unique=True)
    dbUser = models.CharField(max_length=50)

class DBMeta(models.Model):
    database = models.ForeignKey(Databases, on_delete=models.CASCADE)
    key = models.CharField(max_length=200)
    value = models.TextField()
