from django.db import models

# Create your models here.


class Coffees(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    is_alcocol = models.BooleanField()


class Publication(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created_date = models.DateField()



