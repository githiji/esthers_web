from django.db import models

class Tweet(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content