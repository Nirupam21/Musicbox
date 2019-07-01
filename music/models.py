from django.db import models

# Create your models here.

class Upload(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=200)
    file = models.FileField()
    thumbnail = models.FileField()
    file_uploader = models.CharField(max_length=200)