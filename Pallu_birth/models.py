from django.db import models

# Create your models here.


class Wishes(models.Model):
    name=models.CharField(max_length=10)
    relation=models.CharField(max_length=15)
    textarea=models.CharField(max_length=500)