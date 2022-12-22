from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20,null=True, blank=True)
    image = models.ImageField()
    date1 = models.DateField(null=True, blank=True)
    short_decsription = models.CharField(max_length=100)
    long_decsription = models.TextField(default='DESC')
    most_popular = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)





class blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20,null=True, blank=True)
    image = models.ImageField()
    date = models.DateField(null=True, blank=True)
    short_decsription = models.CharField(max_length=100)
    long_decsription = models.TextField(default='DESC')
    most_popular = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
