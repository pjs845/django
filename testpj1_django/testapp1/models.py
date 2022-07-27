from ctypes import addressof
from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=200)
    addr = models.TextField()
    rdate = models.DateTimeField()