from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    songs = models.TextField(max_length=500, null=True)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title