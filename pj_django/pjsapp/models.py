from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=200)
    addr = models.TextField()
    rdate = models.DateTimeField()

class BOARD(models.Model):
    writer = models.CharField(max_length=200)
    email = models.TextField()
    subject = models.TextField()
    content = models.TextField()
    rdate = models.DateTimeField()
    
class MEMBER(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField(null=False, unique=True)
    pwd = models.CharField(max_length=200)
    phone = models.TextField()
    rdate = models.DateTimeField()
    update = models.DateTimeField()