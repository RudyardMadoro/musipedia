from django.db import models
from apis.models import Artist


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artits = models.ManyToManyField(Artist, blank=True)
    ratings=models.IntegerField(default=0)

def __str__(self):
    return self.title