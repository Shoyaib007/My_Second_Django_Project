from django.db import models
from django.urls import reverse,reverse_lazy,path

# Create your models here.
class Musician(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    instrument=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.instrument}"
    def get_absolute_url(self):
        return reverse('first_app:index')



class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE,related_name="Album_list")
    album_name=models.CharField(max_length=100,blank=True)
    release_date=models.DateField(null=True)
    numstarts=models.IntegerField(choices=((1,"good"),(2,"better"),(3,"best")))
    def __str__(self):
        return f"{self.album_name} {self.release_date} {self.numstarts}"

    def get_absolute_url(self):
        return reverse('first_app:index')
