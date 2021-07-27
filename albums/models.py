from django.db import models
from filer.fields.image import FilerImageField
from datetime import date
from apis.models import Artist
from songs.models import Song



# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year =  models.IntegerField(default=date.today().year)
    picture=models.ImageField(width_field=100, height_field=100, null=True, upload_to='albums')
    ratings=models.IntegerField(default=0)
    songs = models.ManyToManyField(Song, blank=True)


def __str__(self):
    return self.title