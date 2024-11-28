from django.db import models

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
    image = models.ImageField(upload_to='crop_images/')

    def __str__(self):
            return self.name
                