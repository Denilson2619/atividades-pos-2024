from django.db import models

# Create your models here.

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
