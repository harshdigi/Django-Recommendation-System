from django.db import models

# Create your models here.
class Team (models.Model):
    name = models.CharField(max_length= 200)
    img = models.ImageField(upload_to='pics')
    desig = models.CharField(max_length=100)
    desc = models.TextField()
    prof = models.JSONField()
