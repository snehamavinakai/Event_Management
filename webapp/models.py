from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=255)
    subject = models.TextField(max_length=25)
    message = models.TextField(max_length=25)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=255,blank=True,null=False)
    email = models.EmailField(max_length=254)
    file = models.FileField()
    message = models.TextField(max_length=25)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name

class Card(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc

class Wedding(models.Model):
    firstname = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField(auto_now_add=False, auto_now=False)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.firstname



class BirthDay(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=25)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name

class Corporate(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=25)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name
