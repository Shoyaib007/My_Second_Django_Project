from django.contrib import admin
from first_app import models
# Register your models here.
admin.site.register(models.Musician)
admin.site.register(models.Album)
