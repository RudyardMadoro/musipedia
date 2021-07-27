from django.db import models
from filer.fields.image import FilerImageField


# Create your models here.
class Artist(models.Model):
    realName = models.CharField(max_length=100)
    stageName = models.CharField(max_length=100)
    recordLabel =  models.CharField(max_length=100)
    dob = models.DateField()
    dod=models.DateField(null=True)
    picture=models.ImageField(width_field=50, height_field=50, null=True, upload_to='breeds')
    ratings=models.IntegerField(default=0)

def __str__(self):
    return self.stageName