from django.db import models
from django.contrib.auth.models import User

class Farm(models.Model):
    name = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    farm_size = models.CharField(max_length=100)


    def __str__(self):
        return self.farm_name
# Create your models here.


class Crop(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
            return self.name
    

class Tweet(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
