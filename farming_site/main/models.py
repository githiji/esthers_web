from django.db import models

class Main(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
# Create your models here.
