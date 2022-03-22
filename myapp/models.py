from django.db import models

# Create your models here.
class user(models.Model):
    username  = models.CharField(max_length=30)
    password  = models.CharField(max_length=30)
    full_name  = models.CharField(max_length=30)
    age  = models.CharField(max_length=30)
    address  = models.CharField(max_length=30)