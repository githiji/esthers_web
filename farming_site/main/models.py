from django.db import models

class Farm(models.Model):
    name = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    farm_size = models.CharField(max_length=100)


    def __str__(self):
        return self.farm_name
# Create your models here.

class Crop(models.Model):
    crop_name = models.CharField(max_length=100)
    crop_quantity = models.IntegerField
    crop_price = models.IntegerField

    def __str__(self):
        return self.crop_name
    