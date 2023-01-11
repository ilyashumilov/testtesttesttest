from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    geolocation = models.CharField(max_length=100, null=True, default=None)
    date = models.DateField(max_length=100, null=True, default=None)
    name = models.CharField(max_length=100, null=True, default=None)


class User(models.Model):
    token = models.CharField(max_length=50)
